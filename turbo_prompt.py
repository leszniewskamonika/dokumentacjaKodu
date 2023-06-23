import openai
import time 


openai.api_key = "<YOUR_API_KEY>" #add your open api key
outputFile = open('prompt_2.txt', 'w')

input_text_1 = "Generate a documentation comment for file: "

input_text_2 = "Create a documentation comment for the following code: "

input_text_3= "Generate a documentation comment for the class in the file: "

input_text_4 = "Documentation comment this file: "

input_text_5 = "How wolud documentations comment to the following code looks like file: "

input_text_6 = "What is the best documentation comment for this code in this file: "

input_text_7 = "Create a documentation commentary for the class that includes documentation quality features such as accuracy completeness, understandability, and includes an example for the file: "

input_text_8 = "Create a documentation for the class that includes documentation quality features such as accuracy, completeness, understandability and includes an example for the file: "

input_text_9 = "Create a documentation commentary that is accurate, complete, understandable, and includes an example for the class on file: "

input_text_10 = "Create documentation that is accurate, complete, understandable and includes an example for the class on file: "

#chatQuestionsStart = [input_text_1, input_text_2, input_text_3, input_text_4, input_text_5, input_text_6]
chatQuestionsStart = [input_text_7, input_text_8, input_text_9, input_text_10]


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



inputQueryNumber = 0
for inputQueryStart in  chatQuestionsStart:
    inputQueryNumber+=1
    for inputFileName in inputFileNames:
            headerString  = f"\n\n######################################\n\nProcessing file {inputFileName}, query {inputQueryNumber}\n"
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
                temperature = 0,
            )      
            outputFile.write(f"Usage:\n")
            outputFile.write(f"\tprompt_tokens: {response['usage']['prompt_tokens']}\n")
            outputFile.write(f"\tcompletion_tokens: {response['usage']['completion_tokens']}\n")
            outputFile.write(f"\ttotal_tokens: {response['usage']['total_tokens']}\n")

            
            outputFile.write(f"\nResponse:\n")
            shortestResponseText = response['choices'][0]['message']['content']
            outputFile.write(shortestResponseText)
            print(response)
            time.sleep(21)

inputFile.close()
outputFile.close()
