"""
main.py
程序入口，交互式信息采集主流程
功能：JD录入、分步采集简历信息、每一步实时预览、调用Agent生成简历、确认保存
"""
from utils.preview import render_resume_preview, show_final_markdown_preview
from utils.file_io import save_resume_markdown
from agent.cv_agent import generate_resume_markdown

def main():
    print("===== AI简历生成Agent =====")
    print("交互式采集信息，支持岗位JD定向优化，边填写边预览简历草稿\n")

    resume_data = {}
    jd_content = ""

    # 第一步：询问是否录入JD
    use_jd = input("是否需要粘贴目标岗位JD进行定向简历优化？Y/N：").strip().upper()
    if use_jd == "Y":
        print("请粘贴岗位招聘JD内容，输入完成后单独一行输入【end】结束录入：")
        lines = []
        while True:
            line = input()
            if line.strip() == "end":
                break
            lines.append(line)
        jd_content = "\n".join(lines)
        print("✅ JD录入完成\n")

    # 分步采集信息，每填一项调用实时预览
    resume_data["name"] = input("请输入你的姓名：").strip()
    render_resume_preview(resume_data)

    resume_data["contact"] = input("请输入联系方式（电话/邮箱）：").strip()
    render_resume_preview(resume_data)

    resume_data["education"] = input("请输入教育背景（学校、专业、入学毕业时间）：").strip()
    render_resume_preview(resume_data)

    resume_data["projects"] = input("请输入项目经历（AI相关项目优先写）：").strip()
    render_resume_preview(resume_data)

    resume_data["skills"] = input("请输入专业技能（Python/Pytorch/RAG等）：").strip()
    render_resume_preview(resume_data)

    resume_data["awards"] = input("请输入荣誉奖项，无则直接回车跳过：").strip()
    render_resume_preview(resume_data)

    print("\n==== 全部信息采集完成，正在调用AI生成简历 ====")
    try:
        final_md = generate_resume_markdown(resume_data, jd_content)
    except Exception as e:
        print(f"❌ AI调用失败：{e}")
        return

    # 展示最终完整简历预览
    show_final_markdown_preview(final_md)
    # 调用保存函数（内置确认弹窗）
    save_resume_markdown(final_md)

    print("\n程序结束")

if __name__ == "__main__":
    main()
