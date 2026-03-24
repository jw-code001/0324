# pip install pymupdf langchain-core langchain-community langchain-text-splitters

# pip install pymupdf langchain-core langchain-community langchain-text-splitters

import fitz  # PyMuPDF
from langchain_core.documents import Document
from langchain_community.document_loaders.base import BaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text_from_pdf(file_path):
    """
    PDF 파일에서 텍스트를 추출합니다.
    """
    try:
        doc = fitz.open(file_path)
        text_list = []
        
        for page in doc:
            # 페이지별 텍스트 추출 (여백이나 불필요한 개행을 어느 정도 정제합니다)
            page_text = page.get_text("text")
            if page_text.strip():
                text_list.append(page_text)
        
        doc.close()
        return "\n".join(text_list)
    
    except Exception as e:
        raise ValueError(f"PDF 읽기 중 오류 발생: {e}")

class PdfLoader(BaseLoader):
    """
    랭체인 표준 BaseLoader를 상속받은 PDF 로더 클래스
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        text = extract_text_from_pdf(self.file_path)
        metadata = {"source": self.file_path}
        return [Document(page_content=text, metadata=metadata)]

# ----------------- 실행 테스트 -----------------
if __name__ == "__main__":
    # 파일 경로는 본인의 환경에 맞게 수정하세요.
    file_name = "./srcdata/./srcdata/2026년도_전통시장_및_상점가_활성화_지원사업_공고문.pdf" 
    
    try:
        print(f"[{file_name}] PDF 텍스트 분석 중...")
        loader = PdfLoader(file_name)
        documents = loader.load()
        
        # 텍스트 분할 (500자 단위)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = text_splitter.split_documents(documents)
        
        print(f"성공! 총 {len(docs)}개의 조각으로 분할되었습니다.\n")
        
        if len(docs) > 0:
            print("--- 정제된 텍스트 추출 미리보기 ---")
            print(docs[0].page_content[:300] + "...") # 첫 부분 300자만 출력
        
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")