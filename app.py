import streamlit as st
from logic import recommend_account, recommend_allocation, generate_tips
from fpdf import FPDF
import base64
import io

# 页面设置
st.set_page_config(page_title="SmartNest 智能理财助手", layout="centered")
st.title("🏡 SmartNest 智能理财推荐")

# --- 多语言切换 ---
lang = st.radio("选择语言 / Choose Language", ["中文", "English"])

# --- 邮箱收集 ---
email = st.text_input("留下你的邮箱，获取PDF报告 / Enter email to receive your report (optional):")

# --- 表单输入 ---
with st.form("user_profile"):
    age = st.selectbox("你的年龄是多少？" if lang == "中文" else "Your age:",
                       ["<25", "25-34", "35-44", "45-54", "55+"])
    income = st.selectbox("年收入（税前）：" if lang == "中文" else "Annual income (before tax):",
                          ["<$40,000", "$40,000-$70,000", "$70,000-$100,000", "$100,000+"])
    risk = st.radio("你更看重什么？" if lang == "中文" else "What do you value more?",
                    ["稳定保本", "稍微波动但增长快", "我能承受亏损，追求高增长"]
                    if lang == "中文"
                    else ["Capital preservation", "Moderate growth", "High risk & growth"])
    accounts = st.multiselect("你目前拥有的账户：" if lang == "中文" else "Accounts you currently have:",
                              ["TFSA", "RRSP", "RESP", "非注册账户", "没有/不知道"]
                              if lang == "中文"
                              else ["TFSA", "RRSP", "RESP", "Non-registered", "None/Not sure"])
    goal = st.selectbox("你的财务目标是？" if lang == "中文" else "Your financial goal:",
                        ["买房", "教育/子女基金", "提前退休", "一般储蓄/增长"]
                        if lang == "中文"
                        else ["Buying a home", "Education fund", "Early retirement", "General savings/growth"])

    submitted = st.form_submit_button("🔍 获取建议" if lang == "中文" else "🔍 Get Recommendation")

# --- 生成报告 PDF 的函数 ---
def generate_pdf(content, lang):
    pdf = FPDF()
    pdf.add_page()

    if lang == "中文":
        # 添加中文字体（需要有 .ttf 文件）
        pdf.add_font("simhei", "", "simhei.ttf", uni=True)
        pdf.set_font("simHei", size=12)
    else:
        pdf.set_font("Arial", size=12)

    for line in content.split('\n'):
        pdf.multi_cell(0, 10, txt=line)

    return pdf.output(dest="S").encode("utf-8")  # 返回 PDF 字节流


# --- 结果输出 ---
if submitted:
    st.subheader("📊 推荐报告" if lang == "中文" else "📊 Personalized Report")

    acc_text = recommend_account(income, accounts, lang)
    alloc_text = recommend_allocation(age, risk, lang)
    tips_text = generate_tips(goal, accounts, lang)

    st.markdown("### 💼 推荐账户" if lang == "中文" else "### 💼 Recommended Accounts")
    st.info(acc_text)

    st.markdown("### 📈 投资配置建议" if lang == "中文" else "### 📈 Asset Allocation")
    st.success(alloc_text)

    st.markdown("### 💡 理财建议" if lang == "中文" else "### 💡 Smart Tips")
    st.write(tips_text)

    # 生成 PDF 并提供下载链接
    final_text = f"SmartNest 理财报告\n\n账户建议:\n{acc_text}\n\n配置建议:\n{alloc_text}\n\n理财建议:\n{tips_text}" \
        if lang == "中文" else f"SmartNest Financial Report\n\nAccount Tips:\n{acc_text}\n\nAllocation:\n{alloc_text}\n\nTips:\n{tips_text}"

    pdf_bytes = generate_pdf(final_text, lang)
    b64_pdf = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="smartnest_report.pdf">📥 下载 PDF 报告 / Download PDF Report</a>'
    st.markdown(href, unsafe_allow_html=True)

    if email:
        st.success("✅ 报告准备完成，你可以下载它。如果留下邮箱，未来我们会发送更新。")
