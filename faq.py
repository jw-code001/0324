import streamlit as st
import json
import os

# 페이지 설정
st.set_page_config(
    page_title="2026 전통시장 지원사업 FAQ",
    page_icon="📢",
    layout="centered"
)

def load_faq_data(file_path):
    """JSON 파일을 읽어오는 함수"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def main():
    st.title("📢 2026년도 전통시장 및 상점가 활성화 지원사업")
    st.subheader("자주 묻는 질문 (FAQ)")
    st.write("사업 신청 전 궁금한 사항을 빠르게 확인해 보세요.")
    st.divider()

    # 1. JSON 데이터 로드 (파일명이 faq.json 가정)
    faq_list = load_faq_data('faq.json')

    if not faq_list:
        st.error("FAQ 데이터를 불러올 수 없습니다. 파일 경로를 확인해주세요.")
        return

    # 2. FAQ 출력 (Expander 형태)
    for item in faq_list:
        with st.expander(f"Q{item['id']}. {item['question']}"):
            st.write(item['answer'])
            # 각 답변마다 '도움이 되었나요?' 같은 인터랙션 추가 가능
            st.caption("이 답변이 도움이 되셨나요? 👍 👎")

    st.divider()

    # 3. 수익화 및 신뢰도를 위한 하단 섹션
    st.info("""
    **💡 안내 및 면책 공고**
    * 본 FAQ는 **2026년도 전통시장 및 상점가 활성화 지원사업 공고문**을 기반으로 AI가 요약한 내용입니다.
    * 정확한 지원 조건 및 신청 서류는 반드시 **중소벤처기업부 공식 공고문 원본**을 확인하시기 바랍니다.
    * 본 서비스는 사용자의 편의를 위해 제공되며, 정보의 오류로 인한 불이익은 책임지지 않습니다.
    """)

    # 광고가 들어갈 자리 (예시)
    st.markdown("---")
    st.write("⊞ [광고] 소상공인을 위한 저금리 대환대출 알아보기")

if __name__ == "__main__":
    main()