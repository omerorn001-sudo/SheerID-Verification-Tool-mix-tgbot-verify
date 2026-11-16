import os
import utils.document_templates as dt
from utils.document_templates import DocumentType

# 1. 固定学校（只保留 miami，不随机选校）
dt.UNIVERSITIES = {'miami': dt.UNIVERSITIES['miami']}

# 2. 固定学生姓名
FIRST_NAME = "shania"
LAST_NAME = "lowe"

# 3. 选择要测试的单个文档类型（可按需改为 CLASS_SCHEDULE 或 TUITION_RECEIPT）
DOC_TYPE = DocumentType.ENROLLMENT_VERIFICATION

from spotify import img_generator as student_gen


def run_single_test():
    os.makedirs("test_output", exist_ok=True)
    img_data = student_gen.generate_image(FIRST_NAME, LAST_NAME, doc_type=DOC_TYPE)
    filename = f"test_output/student_{DOC_TYPE.value}.png"

    with open(filename, "wb") as f:
        f.write(img_data)

    print(f"✓ 生成成功 -> {filename}")


if __name__ == "__main__":
    run_single_test()
