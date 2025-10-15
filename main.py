import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
#from video_detector import process_video
from audio_detector import process_audio

class DeepfakeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deepfake Detection System")
        self.root.geometry("650x500")
        self.root.config(bg="#0E1116")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)

        self.create_widgets()

    def create_widgets(self):
        # --- Title ---
        tk.Label(
            self.root,
            text="Deepfake Detection System",
            font=("Segoe UI", 18, "bold"),
            fg="white", bg="#0E1116"
        ).pack(pady=20)

        # --- Buttons Section ---
        btn_frame = tk.Frame(self.root, bg="#0E1116")
        btn_frame.pack(pady=20)

        #ttk.Button(btn_frame, text="🎥 Detect Video Deepfake", width=25, command=self.load_video).grid(row=0, column=0, padx=20, pady=10)
        ttk.Button(btn_frame, text="🎙️ Detect Audio Deepfake", width=25, command=self.load_audio).grid(row=0, column=1, padx=20, pady=10)

        # --- Progress Bar ---
        self.progress_label = tk.Label(self.root, text="Idle", font=("Segoe UI", 10), fg="#00FF99", bg="#0E1116")
        self.progress_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        # --- Log Area ---
        tk.Label(
            self.root,
            text="Process Log:",
            font=("Segoe UI", 11, "bold"),
            fg="white", bg="#0E1116"
        ).pack(pady=(10, 0))

        self.log_text = tk.Text(self.root, height=10, width=70, bg="#1B1F27", fg="#C0C0C0", insertbackground="white")
        self.log_text.pack(pady=5)
        self.log_text.config(state=tk.DISABLED)

        # --- Result Label ---
        self.result_label = tk.Label(self.root, text="", fg="white", bg="#0E1116", font=("Segoe UI", 14, "bold"))
        self.result_label.pack(pady=15)

        # --- Control Buttons ---
        ttk.Button(self.root, text="Reset", command=self.reset_ui).pack(side="left", padx=100, pady=20)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(side="right", padx=100, pady=20)

    def append_log(self, msg):
        """Append message to log box."""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{msg}\n")
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)

    def update_progress(self, step_text, percent):
        """Update progress bar and label."""
        self.progress_label.config(text=step_text)
        self.progress_bar["value"] = percent
        self.root.update_idletasks()
        self.append_log(step_text)

    '''def load_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
        if file_path:
            self.append_log(f"[Video Selected] {os.path.basename(file_path)}")
            thread = threading.Thread(target=self.run_video_detection, args=(file_path,))
            thread.start() '''

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            self.append_log(f"[Audio Selected] {os.path.basename(file_path)}")
            thread = threading.Thread(target=self.run_audio_detection, args=(file_path,))
            thread.start()

    '''def run_video_detection(self, path):
        self.progress_bar["value"] = 0
        self.update_progress("Initializing video model...", 5)
        try:
            result, conf = process_video(path, self.update_progress)
            self.result_label.config(text=f"Result: {result.upper()} ({conf*100:.2f}%)")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.append_log(f"Error: {e}") '''

    def run_audio_detection(self, path):
        self.progress_bar["value"] = 0
        self.update_progress("Initializing audio model...", 5)
        try:
            result, conf = process_audio(path, self.update_progress)
            self.result_label.config(text=f"Result: {result.upper()}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.append_log(f"Error: {e}")

    def reset_ui(self):
        self.progress_label.config(text="Idle")
        self.progress_bar["value"] = 0
        self.result_label.config(text="")
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.append_log("System reset.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeepfakeGUI(root)
    root.mainloop()
