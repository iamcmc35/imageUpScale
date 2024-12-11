import streamlit as st
from PIL import Image
from io import BytesIO

def resize_image(image, scale):
    # 현재 이미지 크기 가져오기
    width, height = image.size
    
    # 새로운 크기 계산
    new_width = int(width * scale)
    new_height = int(height * scale)

    # 이미지 리사이즈
    resized_image = image.resize((new_width, new_height))
    return resized_image

def main():
    st.title("Image Resizer")
    st.write("Upload an image to resize it.")

    # 이미지 업로드
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # PIL을 사용해 이미지 열기
        image = Image.open(uploaded_file)

        # 원본 이미지 표시
        st.image(image, caption="Original Image", use_column_width=True)

        if st.button("Resize Image (2x)")):
            # 이미지 크기를 2배로 변경
            resized_image = resize_image(image, scale=2)

            # 리사이즈된 이미지 표시
            st.image(resized_image, caption="Resized Image (2x)", use_column_width=True)

            # 다운로드 링크 제공
            buffer = BytesIO()
            resized_image.save(buffer, format="PNG")
            buffer.seek(0)
            st.download_button(
                label="Download Resized Image",
                data=buffer,
                file_name="resized_image.png",
                mime="image/png",
            )

if __name__ == "__main__":
    main()
