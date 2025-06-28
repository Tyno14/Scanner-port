import customtkinter
import threading
from tkinter import filedialog
from scanner import run_scan

import json # Import for JSON export
import xml.etree.ElementTree as ET # Import for XML export
import matplotlib.pyplot as plt # Import for graphing
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Import for embedding matplotlib in Tkinter
from collections import Counter # For counting open ports per IP

class PortScannerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Port Scanner")
        self.geometry("600x700") # Adjusted size back for textbox

        # Initial theme setting (can be changed by user)
        customtkinter.set_appearance_mode("System") # Default to system theme
        customtkinter.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1) # Adjusted row for results textbox

        self.all_scan_results = [] # Store all scan results here

        # --- WIDGETS ---
        self.title_label = customtkinter.CTkLabel(self, text="Port Scanner", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Theme selection
        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 10), sticky="w")
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=0, column=0, padx=(150, 20), pady=(20, 10), sticky="w")
        self.appearance_mode_optionemenu.set("System") # Default value

        self.host_frame = customtkinter.CTkFrame(self)
        self.host_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.host_frame.grid_columnconfigure(1, weight=1)
        self.host_label = customtkinter.CTkLabel(self.host_frame, text="Host/IP/CIDR:")
        self.host_label.grid(row=0, column=0, padx=10, pady=10)
        self.host_entry = customtkinter.CTkEntry(self.host_frame, placeholder_text="e.g., 127.0.0.1, google.com or 192.168.1.0/24")
        self.host_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # --- Presets ---
        self.preset_frame = customtkinter.CTkFrame(self)
        self.preset_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.preset_label = customtkinter.CTkLabel(self.preset_frame, text="Scan Presets:")
        self.preset_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.preset_options = {
            "Custom Range": {"type": "range", "start": 1, "end": 65535},
            "Well-Known Ports": {"type": "range", "start": 1, "end": 1024},
            "Common Web Ports": {"type": "list", "ports": [80, 443, 8080, 8443]},
            "Common Database Ports": {"type": "list", "ports": [1433, 3306, 5432, 27017]},
            "All TCP Ports": {"type": "range", "start": 1, "end": 65535}
        }
        self.preset_menu = customtkinter.CTkOptionMenu(self.preset_frame, values=list(self.preset_options.keys()), command=self.apply_preset)
        self.preset_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.preset_frame.grid_columnconfigure(1, weight=1)
        

        self.port_frame = customtkinter.CTkFrame(self)
        self.port_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.port_frame.grid_columnconfigure((0, 1), weight=1)
        self.start_port_entry = customtkinter.CTkEntry(self.port_frame, placeholder_text="Start Port or List")
        self.start_port_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.end_port_entry = customtkinter.CTkEntry(self.port_frame, placeholder_text="End Port")
        self.end_port_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # --- New Scan Options Frame ---
        self.scan_options_frame = customtkinter.CTkFrame(self)
        self.scan_options_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.scan_options_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Scan Type
        self.scan_type_label = customtkinter.CTkLabel(self.scan_options_frame, text="Scan Type:")
        self.scan_type_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.scan_type_var = customtkinter.StringVar(value="TCP")
        self.tcp_radio = customtkinter.CTkRadioButton(self.scan_options_frame, text="TCP", variable=self.scan_type_var, value="TCP")
        self.tcp_radio.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.udp_radio = customtkinter.CTkRadioButton(self.scan_options_frame, text="UDP", variable=self.scan_type_var, value="UDP")
        self.udp_radio.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Rate Limiting
        self.delay_label = customtkinter.CTkLabel(self.scan_options_frame, text="Scan Delay (s):")
        self.delay_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.delay_entry = customtkinter.CTkEntry(self.scan_options_frame, placeholder_text="0.0 (e.g., 0.1)")
        self.delay_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
        self.delay_entry.insert(0, "0.0") # Default value

        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=5, column=0, padx=20, pady=10)
        self.scan_button = customtkinter.CTkButton(self.buttons_frame, text="Start Scan", command=self.start_scan_thread)
        self.scan_button.pack(side="left", padx=(0, 10))
        self.export_button = customtkinter.CTkButton(self.buttons_frame, text="Export Results", command=self.export_results, state="disabled")
        self.export_button.pack(side="left", padx=(0, 10))
        self.graph_button = customtkinter.CTkButton(self.buttons_frame, text="Show Graph", command=self.show_graph, state="disabled")
        self.graph_button.pack(side="left")

        # Results Textbox
        self.results_textbox = customtkinter.CTkTextbox(self, state="disabled", wrap="word")
        self.results_textbox.grid(row=6, column=0, padx=20, pady=(10, 0), sticky="nsew")

        self.status_label = customtkinter.CTkLabel(self, text="")
        self.status_label.grid(row=7, column=0, padx=20, pady=(5, 5), sticky="w")

        self.progress_bar = customtkinter.CTkProgressBar(self)
        self.progress_bar.grid(row=8, column=0, padx=20, pady=(0, 10), sticky="ew")
        self.progress_bar.set(0)

        self.preset_menu.set("Custom Range")
        self.apply_preset("Custom Range") # Set default port values

    def apply_preset(self, choice):
        selection = self.preset_options[choice]

        # 1. Re-enable both entry fields to ensure they are editable
        self.start_port_entry.configure(state="normal")
        self.end_port_entry.configure(state="normal")

        # 2. Clear both fields
        self.start_port_entry.delete(0, "end")
        self.end_port_entry.delete(0, "end")

        # 3. Fill fields based on preset type
        if selection["type"] == "range":
            self.start_port_entry.insert(0, str(selection["start"]))
            self.end_port_entry.insert(0, str(selection["end"]))
        else:  # It's a list of ports
            self.start_port_entry.insert(0, ",".join(map(str, selection["ports"])))
            # 4. Disable the end_port_entry ONLY for list types
            self.end_port_entry.configure(state="disabled")

    def get_ports_from_input(self):
        if self.start_port_entry.cget('state') == 'disabled':
            # Preset list of ports
            return [int(p) for p in self.start_port_entry.get().split(',') if p.strip().isdigit()]
        else:
            # Range of ports
            start = int(self.start_port_entry.get())
            end = int(self.end_port_entry.get())
            return list(range(start, end + 1))

    def start_scan_thread(self):
        self.scan_button.configure(state="disabled")
        self.export_button.configure(state="disabled")
        self.graph_button.configure(state="disabled") # Disable graph button at start of scan
        # Clear previous results from the textbox
        self.all_scan_results = [] # Clear all results
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        self.results_textbox.configure(state="disabled")

        self.status_label.configure(text="")
        self.progress_bar.set(0)

        try:
            host_or_subnet = self.host_entry.get()
            ports_to_scan = self.get_ports_from_input()
            scan_delay = float(self.delay_entry.get())
            scan_type = self.scan_type_var.get()

            if not host_or_subnet or not ports_to_scan:
                self.update_status("Error: Host/CIDR and ports cannot be empty.")
                self.scan_button.configure(state="normal")
                return

            thread = threading.Thread(
                target=run_scan,
                args=(
                    host_or_subnet,
                    ports_to_scan,
                    self.update_status,
                    self.add_result,
                    self.on_scan_finished,
                    self.update_progress,
                    scan_delay,
                    scan_type
                ),
                daemon=True
            )
            thread.start()

        except ValueError as e:
            self.update_status(f"Error: Invalid input. {e}")
            self.scan_button.configure(state="normal")
        except Exception as e:
            self.update_status(f"An unexpected error occurred: {e}")
            self.scan_button.configure(state="normal")

    def add_result(self, message, ip_address=None, port_number=None, banner=None, port_type=None, service=None):
        # This needs to be thread-safe, so we schedule it to run in the main loop
        self.after(0, self._add_result_ui, message, ip_address, port_number, banner, port_type, service)

    def _add_result_ui(self, message, ip_address, port_number, banner, port_type, service):
        # Only add to textbox if it's a valid scan result (not a status message)
        if port_number is not None and ip_address is not None:
            self.all_scan_results.append({"ip": ip_address, "port": port_number, "banner": banner, "type": port_type, "service": service})
            self.results_textbox.configure(state="normal")
            self.results_textbox.insert("end", f"IP: {ip_address}, Port: {port_number}/{port_type} ({service}): {banner}\n")
            self.results_textbox.configure(state="disabled")
            self.results_textbox.see("end")
        else:
            # For status messages, still display them in the status label
            self.update_status(message)

    def update_status(self, message):
        self.after(0, lambda: self.status_label.configure(text=message))

    def update_progress(self, value):
        self.after(0, lambda: self.progress_bar.set(value))

    def on_scan_finished(self):
        self.after(0, self._on_scan_finished_ui)

    def _on_scan_finished_ui(self):
        self.scan_button.configure(state="normal")
        if self.all_scan_results:
            self.export_button.configure(state="normal")
            self.graph_button.configure(state="normal") # Enable graph button after scan finishes

    def export_results(self):
        host = self.host_entry.get() or "unknown_target"
        filename = filedialog.asksaveasfilename(
            initialfile=f"scan_results_{host}.txt",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("JSON Files", "*.json"), ("XML Files", "*.xml"), ("All Files", "*.* ")]
        )
        if not filename:
            return
            
        try:
            with open(filename, "w", newline='') as f:
                if filename.endswith('.csv'):
                    import csv
                    writer = csv.writer(f)
                    writer.writerow(["IP Address", "Port", "Type", "Service", "Banner"])
                    for detail in sorted(self.all_scan_results, key=lambda x: (x['ip'], x['port'])):
                        writer.writerow([detail['ip'], detail['port'], detail['type'], detail['service'], detail['banner']])
                elif filename.endswith('.json'):
                    json.dump(sorted(self.all_scan_results, key=lambda x: (x['ip'], x['port'])), f, indent=4)
                elif filename.endswith('.xml'):
                    root = ET.Element("ScanResults")
                    for detail in sorted(self.all_scan_results, key=lambda x: (x['ip'], x['port'])):
                        item = ET.SubElement(root, "Result")
                        ET.SubElement(item, "IPAddress").text = str(detail['ip'])
                        ET.SubElement(item, "Port").text = str(detail['port'])
                        ET.SubElement(item, "Type").text = str(detail['type'])
                        ET.SubElement(item, "Service").text = str(detail['service'])
                        ET.SubElement(item, "Banner").text = str(detail['banner'])
                    ET.ElementTree(root).write(f, encoding='unicode', pretty_print=True)
                else:
                    f.write(f"Scan results for {host}:\n\n")
                    for detail in sorted(self.all_scan_results, key=lambda x: (x['ip'], x['port'])):
                        f.write(f"IP: {detail['ip']}, Port: {detail['port']}/{detail['type']} ({detail['service']}): {detail['banner']}\n")
            self.update_status(f"Results exported to {filename}")
        except Exception as e:
            self.update_status(f"Error exporting results: {e}")

    def show_graph(self):
        if not self.all_scan_results:
            self.update_status("No scan results to graph.")
            return

        # Count open ports per IP
        ip_counts = Counter(d["ip"] for d in self.all_scan_results)
        ips = list(ip_counts.keys())
        counts = list(ip_counts.values())

        # Create a new top-level window for the graph
        graph_window = customtkinter.CTkToplevel(self)
        graph_window.title("Open Ports per IP")
        graph_window.geometry("700x500")
        graph_window.grid_columnconfigure(0, weight=1)
        graph_window.grid_rowconfigure(0, weight=1)

        # Create matplotlib figure and axes
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(ips, counts, color='skyblue')
        ax.set_xlabel("IP Address")
        ax.set_ylabel("Number of Open Ports")
        ax.set_title("Open Ports per IP Address")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Embed the plot in the CustomTkinter window
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        canvas.draw()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)