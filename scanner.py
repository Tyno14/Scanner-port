import socket
import time
import ipaddress

# Common port to service mapping for basic service detection
COMMON_PORTS = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    111: "RPCBind",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB/CIFS (Microsoft-DS)",
    500: "ISAKMP (IKE)",
    514: "Syslog",
    520: "RIP",
    636: "LDAPS",
    1433: "Microsoft SQL Server",
    1521: "Oracle Listener",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP (Remote Desktop Protocol)",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Proxy/Tomcat"
}

def get_banner(sock):
    try:
        sock.settimeout(2.0)
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner
    except (socket.timeout, ConnectionResetError):
        return ""
    except Exception as e:
        return f"(Could not get banner: {e})"

def scan_udp_port(target_ip, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(timeout)
            # Send a small packet to provoke a response or ICMP error
            sock.sendto(b"", (target_ip, port))
            data, addr = sock.recvfrom(1024)
            return True, "Open (Response received)"
    except socket.timeout:
        return False, "Filtered/Closed (No response)"
    except socket.error as e:
        # Check for specific error messages indicating closed/filtered ports
        if "Connection refused" in str(e) or "Port unreachable" in str(e):
            return False, "Closed (ICMP Port Unreachable)"
        return False, f"Error: {e}"

def resolve_targets(target_input):
    ips_to_scan = []
    try:
        # Try to interpret as a network (CIDR)
        network = ipaddress.ip_network(target_input, strict=False)
        for ip in network.hosts():
            ips_to_scan.append(str(ip))
    except ValueError:
        # If not a network, assume it's a single host
        try:
            ips_to_scan.append(socket.gethostbyname(target_input))
        except socket.gaierror:
            raise ValueError(f"Could not resolve host: {target_input}")
    return ips_to_scan

def run_scan(host_or_subnet, ports_to_scan, status_callback, result_callback, finished_callback, progress_callback, delay=0, scan_type="TCP"):
    status_callback(f"Resolving targets for {host_or_subnet}...")
    try:
        target_ips = resolve_targets(host_or_subnet)
    except ValueError as e:
        status_callback(f"Error: {e}")
        finished_callback()
        return

    total_ips = len(target_ips)
    overall_progress_counter = 0

    for ip_index, target_ip in enumerate(target_ips):
        status_callback(f"Scanning {target_ip} ({scan_type})...")
        result_callback(f"\n--- Scanning {target_ip} ---", ip_address=target_ip, port_number=None, banner=None, port_type=None, service=None)
        open_ports_details = []

        total_ports_per_ip = len(ports_to_scan)
        for i, port in enumerate(ports_to_scan):
            service = COMMON_PORTS.get(port, "Unknown")
            status_callback(f"Scanning port {port} ({service}) on {target_ip}...")
            try:
                if scan_type == "TCP":
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                            sock.settimeout(0.5)
                            result = sock.connect_ex((target_ip, port))
                            if result == 0:
                                banner = get_banner(sock)
                                details = {"ip": target_ip, "port": port, "banner": banner, "type": "TCP", "service": service}
                                open_ports_details.append(details)
                                
                                result_text = f"Port {port}/TCP: Open"
                                if service != "Unknown":
                                    result_text += f" ({service})"
                                if banner:
                                    result_text += f" (Banner: {banner})"
                                result_callback(result_text, ip_address=target_ip, port_number=port, banner=banner, port_type="TCP", service=service)

                    except socket.error as e:
                        pass # connect_ex already handles most connection errors by returning a non-zero code
                elif scan_type == "UDP":
                    is_open, status_msg = scan_udp_port(target_ip, port)
                    if is_open:
                        details = {"ip": target_ip, "port": port, "banner": status_msg, "type": "UDP", "service": service}
                        open_ports_details.append(details)
                        result_callback(f"Port {port}/UDP: {status_msg} ({service})", ip_address=target_ip, port_number=port, banner=status_msg, port_type="UDP", service=service)
                    else:
                        result_callback(f"Port {port}/UDP: {status_msg} ({service})", ip_address=target_ip, port_number=port, banner=status_msg, port_type="UDP", service=service)
            except Exception as e:
                # Catch any unexpected errors during the scan of a single port
                status_callback(f"Error during scan of port {port} on {target_ip}: {e}")
            finally:
                overall_progress_counter += 1
                progress_callback(overall_progress_counter / (total_ips * total_ports_per_ip))
                if delay > 0:
                    time.sleep(delay)
        
        if open_ports_details:
            status_callback(f"Scan of {target_ip} finished. Found {len(open_ports_details)} open port(s).")
        else:
            status_callback(f"Scan of {target_ip} finished. No open ports found.")

    status_callback("Overall scan finished.")
    finished_callback()