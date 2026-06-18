import streamlit as st
import pipeline

st.title("AI 資格教材ジェネレーター")

certification = st.text_input(
    "資格名",
    value="AWS Certified AI Practitioner",
    placeholder="例: AWS Certified AI Practitioner",
)

if st.button("生成開始", disabled=not certification.strip()):
    with st.status("教材を生成中...", expanded=True) as status:
        st.write("Research Agent を実行中...")
        try:
            logs, content = pipeline.run(certification.strip())
            for entry in logs:
                st.write(entry)
            status.update(label="生成完了！", state="complete")
        except Exception as e:
            status.update(label="エラーが発生しました", state="error")
            st.error(str(e))
            st.stop()

    st.subheader("生成された教材")
    st.markdown(content)

    st.download_button(
        label="Markdown でダウンロード",
        data=content.encode("utf-8"),
        file_name="textbook.md",
        mime="text/markdown",
    )
