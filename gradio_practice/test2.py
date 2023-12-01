import gradio as gr
#該函數有3個輸入和2個輸出
def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)
demo = gr.Interface(
    fn=greet,
    #設定輸入元件
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    #輸出元件
    outputs=["text", "number"],
)
demo.launch()