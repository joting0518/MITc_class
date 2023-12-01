import gradio as gr

def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
)

if __name__ == "__main__":
    app, local_url, share_url = iface.launch(share=True)
    print(f"Running on local URL: {local_url}")
    print(f"To access from another device, use the shareable link: {share_url}")
