import customtkinter
import threading
from tkinter import filedialog
from scanner import run_scan

class PortScannerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Port Scanner")
        self.geometry("550x700") # Adjusted size

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1) # Adjusted row for results textbox

        self.open_ports_details = []

        # --- WIDGETS ---
        self.title_label = customtkinter.CTkLabel(self, text="Port Scanner", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.host_frame = customtkinter.CTkFrame(self)
        self.host_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.host_frame.grid_columnconfigure(1, weight=1)
        self.host_label = customtkinter.CTkLabel(self.host_frame, text="Host/IP:")
        self.host_label.grid(row=0, column=0, padx=10, pady=10)
        self.host_entry = customtkinter.CTkEntry(self.host_frame, placeholder_text="e.g., 127.0.0.1 or google.com")
        self.host_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # --- Presets ---
        self.preset_frame = customtkinter.CTkFrame(self)
        self.preset_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.preset_label = customtkinter.CTkLabel(self.preset_frame, text="Scan Presets:")
        self.preset_label.pack(side="left", padx=10, pady=10)

        self.preset_options = {
            "Custom Range": {"type": "range", "start": 1, "end": 65535},
            "Well-Known Ports": {"type": "range", "start": 1, "end": 1024},
            "Common Web Ports": {"type": "list", "ports": [80, 443, 8080, 8443]},
            "Common Database Ports": {"type": "list", "ports": [1433, 3306, 5432, 27017]},
            "All TCP Ports": {"type": "range", "start": 1, "end": 65535}
        }
        self.preset_menu = customtkinter.CTkOptionMenu(self.preset_frame, values=list(self.preset_options.keys()), command=self.apply_preset)
        self.preset_menu.pack(side="left", padx=10, pady=10, fill="x", expand=True)
        

        self.port_frame = customtkinter.CTkFrame(self)
        self.port_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.port_frame.grid_columnconfigure((0, 1), weight=1)
        self.start_port_entry = customtkinter.CTkEntry(self.port_frame, placeholder_text="Start Port or List")
        self.start_port_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.end_port_entry = customtkinter.CTkEntry(self.port_frame, placeholder_text="End Port")
        self.end_port_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=4, column=0, padx=20, pady=10)
        self.scan_button = customtkinter.CTkButton(self.buttons_frame, text="Start Scan", command=self.start_scan_thread)
        self.scan_button.pack(side="left", padx=(0, 10))
        self.export_button = customtkinter.CTkButton(self.buttons_frame, text="Export Results", command=self.export_results, state="disabled")
        self.export_button.pack(side="left")

        self.results_textbox = customtkinter.CTkTextbox(self, state="disabled", wrap="word")
        self.results_textbox.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="nsew")

        self.status_label = customtkinter.CTkLabel(self, text="")
        self.status_label.grid(row=6, column=0, padx=20, pady=(5, 5), sticky="w")

        self.progress_bar = customtkinter.CTkProgressBar(self)
        self.progress_bar.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")
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
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        self.results_textbox.configure(state="disabled")
        self.status_label.configure(text="")
        self.progress_bar.set(0)
        self.open_ports_details = []

        try:
            host = self.host_entry.get()
            ports_to_scan = self.get_ports_from_input()

            if not host or not ports_to_scan:
                self.update_status("Error: Host and ports cannot be empty.")
                self.scan_button.configure(state="normal")
                return

            thread = threading.Thread(
                target=run_scan,
                args=(host, ports_to_scan, self.update_status, self.add_result, self.on_scan_finished, self.update_progress),
                daemon=True
            )
            thread.start()

        except ValueError:
            self.update_status("Error: Invalid port numbers.")
            self.scan_button.configure(state="normal")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
            self.scan_button.configure(state="normal")

    def add_result(self, message, port_number=None, banner=None):
        # This needs to be thread-safe, so we schedule it to run in the main loop
        self.after(0, self._add_result_ui, message, port_number, banner)

    def _add_result_ui(self, message, port_number, banner):
        self.results_textbox.configure(state="normal")
        self.results_textbox.insert("end", message + "\n")
        self.results_textbox.configure(state="disabled")
        self.results_textbox.see("end")
        if port_number is not None:
            self.open_ports_details.append({"port": port_number, "banner": banner})

    def update_status(self, message):
        self.after(0, lambda: self.status_label.configure(text=message))

    def update_progress(self, value):
        self.after(0, lambda: self.progress_bar.set(value))

    def on_scan_finished(self):
        self.after(0, self._on_scan_finished_ui)

    def _on_scan_finished_ui(self):
        self.scan_button.configure(state="normal")
        if self.open_ports_details:
            self.export_button.configure(state="normal")

    def export_results(self):
        host = self.host_entry.get() or "unknown_host"
        filename = filedialog.asksaveasfilename(
            initialfile=f"scan_results_{host}.txt",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("All Files", "*.* ")]
        )
        if not filename:
            return
            
        try:
            with open(filename, "w", newline='') as f:
                if filename.endswith('.csv'):
                    import csv
                    writer = csv.writer(f)
                    writer.writerow(["Port", "Status", "Banner"])
                    for detail in sorted(self.open_ports_details, key=lambda x: x['port']):
                        writer.writerow([detail['port'], "Open", detail['banner']])
                else:
                    f.write(f"Scan results for {host}:\n\n")
                    for detail in sorted(self.open_ports_details, key=lambda x: x['port']):
                        f.write(f"Port {detail['port']}: Open")
                        if detail['banner']:
                            f.write(f" - Banner: {detail['banner']}")
                        f.write("\n")
            self.update_status(f"Results exported to {filename}")
        except Exception as e:
            self.update_status(f"Error exporting results: {e}")