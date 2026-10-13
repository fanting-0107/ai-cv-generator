"""
utils/file_io.py
文件读写工具模块：接收简历，用户确认保存
"""
import os
from datetime import datetime


def save_resume_markdown(md_content: str) -> bool:
    """
    将简历markdown内容保存到 output_cv 文件夹
    :param md_content: AI生成的完整简历markdown字符串
    :return: bool，True=保存成功，False=放弃保存
    """
    # 创建输出目录，如果目录不存在
    output_dir = "output_cv"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # 文件名：简历_时间戳.md，避免重名覆盖
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"resume_{timestamp}.md"
    full_path = os.path.join(output_dir, file_name)

    # 用户确认环节
    user_confirm = input("\n是否确认保存这份简历到本地文件？输入 Y 保存，其他任意字符取消：").strip().upper()
    if user_confirm != "Y":
        print("已取消保存，不会生成简历文件。")
        return False

    # 写入文件
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ 简历保存成功！文件路径：{full_path}")
    return True
