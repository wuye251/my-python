import asyncio

async def fetch_data():
    print("开始获取数据...")
    await asyncio.sleep(2)  # 模拟异步I/O操作
    print("数据获取完成")
    return {"data": 123}

async def main():
    print("主函数开始")
    result = await fetch_data()
    print(f"获取的结果: {result}")
    print("主函数结束")

# print(1)
# asyncio.run(main())
# print(2)

