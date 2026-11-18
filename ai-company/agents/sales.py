from pathlib import Path
from crewai import Agent, Task, Crew, LLM

KNOWLEDGE = Path(__file__).with_name("knowledge.md").read_text(encoding="utf-8")

llm = LLM(model="gemini/gemini-2.5-flash")

sales_agent = Agent(
    role="وكيل مبيعات",
    goal=f"الرد على استفسارات العملاء بناءً على هذه المعرفة:\n{KNOWLEDGE}\nمساعدة العميل وتقديم اللغة المناسبة وعروض تجريبية مجانية عند الاقتضاء. لا تختلق معلومات خارج هذه المعرفة.",
    backstory="مساعد مبيعات ذكي ومحترف لمتجرك.",
    llm=llm,
    allow_delegation=False,
)

def reply_to(message: str) -> str:
    task = Task(
        description=f"الرد على رسالة العميل التالية بشكل احترافي وودود:\n{message}",
        expected_output="رد جاهز للإرسال للعميل.",
        agent=sales_agent,
    )
    result = Crew(agents=[sales_agent], tasks=[task]).kickoff()
    return str(result)