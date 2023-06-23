import openai

openai.api_key = "<YOUR_API_KEY>" #add your api key


file = open('proxy.py', 'r')
all_of_it = file.read()

link = str(all_of_it)

input_text_1 = "Generate a documentation comment for file: "+ link 

input_text_2 = "Create a documentation comment for the following code: " + link

input_text_3= "Generate a documentation comment for the class in the file: "+ link

input_text_4 = "Documentation comment this file: "+ link

input_text_5 = "How wolud documentations comment to the following code looks like file: "+ link

input_text_6 = "What is the best documentation comment for this code in this file: "+ link

#############################################################################################

input_text_7 = "Create a documentation commentary for the class that includes documentation quality features such as accuracy completeness, understandability, and includes an example for the file: "+ link

input_text_8 = "Create a documentation for the class that includes documentation quality features such as accuracy, completeness, understandability and includes an example for the file: " + link

input_text_9 = "Create a documentation commentary that is accurate, complete, understandable, and includes an example for the class on file: " + link

input_text_10 = "Create documentation that is accurate, complete, understandable and includes an example for the class on file: " + link

param_temperature_1 = 0
param_temperature_2 = 0.5
param_temperature_3 = 1


param_system_1 = "You are a helpful assistant."

param_assistant_1 = """
Documentation:

The code above defines three classes: Customer, IChannel, Channel, and ProxyChannel.

The Customer class has a constructor that takes an age parameter and initializes a private attribute called __age. It also has a method called get_age that returns the value of __age.

The IChannel class is an abstract base class that defines a single abstract method called provide_broadcast. This method has a docstring that simply says "broadcasting".

The Channel class is a concrete implementation of the IChannel interface. It overrides the provide_broadcast method and simply prints the message "Broadcast started...".

The ProxyChannel class is another implementation of the IChannel interface. It takes a Customer object as a parameter in its constructor and initializes a private attribute called customer with it. It also initializes a Channel object and stores it in a private attribute called channel.

The ProxyChannel class overrides the provide_broadcast method and first checks the age of the customer by calling the get_age method. If the customer is over 18, it calls the provide_broadcast method of the channel object and prints the message "this service is registered for billing.". If the customer is under 18, it simply prints the message "sorry, this service is not allowed for the customers under the age of 18.".

Example:

Here's an example of how to use these classes:

# create a customer object with age 20
customer = Customer(20)

# create a proxy channel object with the customer object
proxy_channel = ProxyChannel(customer)

# call the provide_broadcast method of the proxy channel object
proxy_channel.provide_broadcast()

# output: 
# Broadcast started...
# this service is registered for billing.

In this example, we create a Customer object with age 20 and a ProxyChannel object with the Customer object. We then call the provide_broadcast method of the ProxyChannel object, which checks the age of the customer and calls the provide_broadcast method of the Channel object if the customer is over 18. The output shows that the broadcast started and the service is registered for billing.
         """


response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
     {"role": "system", "content": "You are a helpful assistant"},
     {"role": "user", "content": input_text_10},
     {"role": "assistant", "content":  param_assistant_1},
     {"role": "user", "content": "Improve the created answer by completing the description so that the created documentation has the characteristics of high quality documentation."}
     ],
    temperature = 0,
)

output_text = response['choices'][0]['message']['content']

output_text_1 = response['usage']['completion_tokens']
output_text_2 = response['usage']['prompt_tokens']
output_text_3 = response['usage']['total_tokens']

print(output_text_1)
print(output_text_2)
print(output_text_3)
print(output_text)


file.close()

