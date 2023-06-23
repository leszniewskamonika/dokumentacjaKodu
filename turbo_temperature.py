import openai
import time 

openai.api_key = "<YOUR_API_KEY>" #add your open api key
outputFile = open('raport.txt', 'w')

input_text_9 = "Create a documentation commentary that is accurate, complete, understandable, and includes an example for the class on file: "
input_text_10 = "Create documentation that is accurate, complete, understandable and includes an example for the class on file: "
chatQuestionsStart = [input_text_9, input_text_10]

temperatures = [0, 0.5, 1]
inputFileNames = ["room.py"
        ,"fibo.py"
        ,"pascal.py"
        ,"island.py"
        ,"calculate.py"
        ,"english.py"
        ,"mycalendar.py"
        ,"solution.py"
        ,"person.py"
        ,"proxy.py"
        ]        

def getShortestResponseIndex(choices):
    min = float('inf')
    index = -1
    for currentIdx, choice in enumerate(choices):
        length = len(choice['message']['content'])
        if length < min:
            min = length
            index = currentIdx
    return index

inputQueryNumber = 0
for inputQueryStart in  chatQuestionsStart:
    inputQueryNumber+=1
    for inputFileName in inputFileNames:
        for temp in temperatures:
            headerString  = f"\n\n######################################\n\nProcessing file {inputFileName}, for temperature {temp} and query {inputQueryNumber}\n"
            print(headerString)

            outputFile.write(headerString)
            
            inputFile = open(inputFileName, 'r')
            inputFileContent = inputFile.read()
            inputFileContentStr = str(inputFileContent)

            chatQuestion = inputQueryStart + inputFileContentStr
            
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=[
                {"role": "user", "content": chatQuestion},
                ],
                temperature = temp,
                n = 3,
                #max_tokens = 200
            )      
            outputFile.write(f"Usage:\n")
            outputFile.write(f"\tprompt_tokens: {response['usage']['prompt_tokens']}\n")
            outputFile.write(f"\tcompletion_tokens: {response['usage']['completion_tokens']}\n")
            outputFile.write(f"\ttotal_tokens: {response['usage']['total_tokens']}\n")

            shortestResponseIndex = getShortestResponseIndex(response['choices'])
            outputFile.write(f"\nShortest resposne:\n")
            shortestResponseText = response['choices'][shortestResponseIndex]['message']['content']
            outputFile.write(shortestResponseText)
            print(response)
            time.sleep(21)

inputFile.close()
outputFile.close()
