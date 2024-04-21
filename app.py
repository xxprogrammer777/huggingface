from transformers import pipeline
import gradio as gr

# تحميل نموذج الترجمة
translator = pipeline("translation_en_ar", model="Helsinki-NLP/opus-mt-en-ar")

# تعريف دالة الترجمة
def translate_text(text):
    result = translator(text)[0]["translation_text"]
    return result

# بناء واجهة المستخدم
iface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=2, placeholder="أدخل النص الإنجليزي هنا"),
    outputs="text",
    title="مترجم إنجليزي-عربي",
    description="قم بترجمة النصوص من الإنجليزية إلى العربية",
)

# تشغيل التطبيق
iface.launch()
