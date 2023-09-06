from PIL import Image, ImageFilter

input_image_path = "V006_77_1_19_11_03_12_1_4521q_20201209_8.jpeg"  # 입력 이미지 파일 경로


def apply_blur(input_path, output_path, blur_radius=2):
    try:
        image = Image.open(input_path)
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
        blurred_image.save(output_path)
        print("이미지 블러 효과가 적용되었습니다.")
    except Exception as e:
        print("블러 효과 적용 중 오류가 발생했습니다:", e)


# 입력 이미지 경로와 출력 이미지 경로를 지정합니다.
input_image_path = "V006_77_1_19_11_03_12_1_4521q_20201209_8.jpeg"
output_image_path = "blurred_image.jpg"

# 블러 반경을 설정하여 이미지에 블러 효과를 적용합니다.
apply_blur(input_image_path, output_image_path, blur_radius=20)
