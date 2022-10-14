from filter_names import Filter

filtered_names = Filter()

with open("Input/Letters/starting_letter.docx", mode="r") as file:
    message_before_edite = file.read()

for i in range(len(filtered_names.names)):
    message_after_edite = message_before_edite.replace("[name]", filtered_names.names[i])
    with open(f"Output/ReadyToSend/{filtered_names.names[i]}.docx", "w") as file:
        file.write(message_after_edite)
