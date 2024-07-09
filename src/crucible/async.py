# import ollama
# import time
# import asyncio
# from ollama import AsyncClient

# MODEL = "phi3"
# PROMPT = "Why is the sky blue?"


# def main():
#     start_time = time.perf_counter()
#     print(f"Query {MODEL}...")

#     try:
#         response = asyncio.run(query(MODEL, PROMPT))
#     except ollama.ResponseError as e:
#         print("Error:", e.error)

#     print(response["message"]["content"])  # type: ignore
#     end_time = time.perf_counter()
#     print(f"Time taken: {end_time - start_time:.2f} seconds")


# async def query(model, prompt):
#     response = await AsyncClient().chat(
#         model=model,
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt,
#             },
#         ],
#     )
#     return response


# if __name__ == "__main__":
#     main()
