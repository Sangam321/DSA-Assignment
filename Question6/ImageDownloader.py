import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
from concurrent.futures import ThreadPoolExecutor
import requests
from PIL import Image, ImageTk
from io import BytesIO

class ImageDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Downloader")

        self.url_label = ttk.Label(root, text="Enter URLs (separated by commas):")
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.download_button = ttk.Button(root, text="Download", command=self.download_images)
        self.download_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        self.pause_button = ttk.Button(root, text="Pause", state="disabled", command=self.pause_download)
        self.pause_button.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        self.resume_button = ttk.Button(root, text="Resume", state="disabled", command=self.resume_download)
        self.resume_button.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)

        self.cancel_button = ttk.Button(root, text="Cancel", state="disabled", command=self.cancel_download)
        self.cancel_button.grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)

        self.progress_label = ttk.Label(root, text="Progress:")
        self.progress_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.progressbar = ttk.Progressbar(root, orient=tk.HORIZONTAL, mode='determinate')
        self.progressbar.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky=tk.W+tk.E)

        self.images_frame = ttk.Frame(root)
        self.images_frame.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky=tk.W+tk.E)

        self.lock = threading.Lock()
        self.thread_pool = ThreadPoolExecutor(max_workers=5)
        self.download_tasks = []

    def download_images(self):
        urls = self.url_entry.get().split(',')
        for url in urls:
            if url.strip():
                self.progressbar['value'] = 0
                self.download_button['state'] = "disabled"
                self.pause_button['state'] = "normal"
                self.cancel_button['state'] = "normal"
                task = self.thread_pool.submit(self.download_image, url.strip())
                self.download_tasks.append(task)

    def pause_download(self):
        for task in self.download_tasks:
            task.cancel()
        self.download_button['state'] = "normal"
        self.pause_button['state'] = "disabled"
        self.resume_button['state'] = "normal"
        self.cancel_button['state'] = "disabled"

    def resume_download(self):
        urls = self.url_entry.get().split(',')
        for url in urls:
            if url.strip():
                self.progressbar['value'] = 0
                self.download_button['state'] = "disabled"
                self.pause_button['state'] = "normal"
                self.resume_button['state'] = "disabled"
                self.cancel_button['state'] = "normal"
                task = self.thread_pool.submit(self.download_image, url.strip())
                self.download_tasks.append(task)

    def cancel_download(self):
        self.thread_pool.shutdown(wait=False)
        self.download_button['state'] = "normal"
        self.pause_button['state'] = "disabled"
        self.resume_button['state'] = "disabled"
        self.cancel_button['state'] = "disabled"
        self.progressbar['value'] = 0

    def download_image(self, url):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with self.lock:
                    image_bytes = BytesIO(response.content)
                    image = Image.open(image_bytes)
                    photo_image = ImageTk.PhotoImage(image)

                    image_label = ttk.Label(self.images_frame, image=photo_image)
                    image_label.image = photo_image
                    image_label.grid(row=len(self.download_tasks), column=0, padx=5, pady=5)

                    self.progressbar['value'] = 100
            else:
                messagebox.showerror("Error", f"Failed to download image {url}. Invalid URL or network issue.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to download image {url}: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred while downloading image {url}: {str(e)}")
        finally:
            self.download_button['state'] = "normal"
            self.pause_button['state'] = "disabled"
            self.resume_button['state'] = "disabled"
            self.cancel_button['state'] = "disabled"

def main():
    root = tk.Tk()
    app = ImageDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
