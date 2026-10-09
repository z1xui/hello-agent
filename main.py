# 极简 agent 示例，无需 API Key
def reply(q: str) -> str:
    q = q.strip()
    if not q:
        return "你好，我是 hello-agent，有什么可以帮你？"
    return f"收到：{q}（demo 回显，接入 LLM 即可变真 agent）"

if __name__ == "__main__":
    print(reply("你好"))
    try:
        while True:
            s = input("> ")
            if s in ("quit", "exit"):
                break
            print(reply(s))
    except (EOFError, KeyboardInterrupt):
        pass
