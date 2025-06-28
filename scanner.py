import socket

def get_banner(sock):
    try:
        sock.settimeout(2.0)
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner
    except (socket.timeout, ConnectionResetError):
        return ""
    except Exception as e:
        return f"(Could not get banner: {e})"

def run_scan(host, ports_to_scan, status_callback, result_callback, finished_callback, progress_callback):
    status_callback(f"Scanning {host}...")
    open_ports_details = []
    try:
        target_ip = socket.gethostbyname(host)
        result_callback(f"Resolved {host} to {target_ip}", banner=None)

        total_ports = len(ports_to_scan)
        for i, port in enumerate(ports_to_scan):
            status_callback(f"Scanning port {port}...")
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex((target_ip, port))
                    if result == 0:
                        banner = get_banner(sock)
                        details = {"port": port, "banner": banner}
                        open_ports_details.append(details)
                        
                        result_text = f"Port {port}: Open"
                        if banner:
                            result_text += f" (Banner: {banner})"
                        result_callback(result_text, port_number=port, banner=banner)

            except socket.error as e:
                # Log per-port error if needed, but don't stop the scan
                pass
            finally:
                progress_callback((i + 1) / total_ports)

    except socket.gaierror:
        status_callback(f"Error: Hostname could not be resolved.")
    except Exception as e:
        status_callback(f"An unexpected error occurred: {e}")

    if open_ports_details:
        status_callback(f"Scan finished. Found {len(open_ports_details)} open port(s).")
    else:
        status_callback("Scan finished. No open ports found.")

    finished_callback()