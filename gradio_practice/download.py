import gradio as gr
import os
import zipfile

def download_files(selected_files):
    selected_files = [f.strip() for f in selected_files]

    #創建一個zip檔
    zip_filename = 'downloaded_files.zip'
    #開起zip的寫入模式
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        #對用戶選的file進行操作
        for file in selected_files:
            if os.path.exists(file):
                zip_file.write(file, os.path.basename(file))
            else:
                print(f"File '{file}' not found!")

    return zip_filename

iface = gr.Interface(
    fn=download_files,
    inputs=[
        gr.CheckboxGroup(
            choices=["data/file1.txt", "data/file2.txt", "data/file3.txt"],
            type="value",
            label="Select files to download"
        )
    ],
    outputs=gr.File(label="Download Zip"),
    live=True
)

if __name__ == "__main__":
    app, local_url, share_url = iface.launch(share=True)
    print(f"Running on local URL: {local_url}")
    print(f"To access from another device, use the shareable link: {share_url}")