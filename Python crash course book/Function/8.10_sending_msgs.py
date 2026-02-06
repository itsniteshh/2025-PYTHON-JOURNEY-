msgs = ["Hello", "Hii", "Howdy", "Bonjour"]
sent_msgs = []

def send_msgs(msgs, sent_msgs):
    
    while msgs:
        sending_msgs = msgs.pop()
        print(f"Sending, {sending_msgs}")
        sent_msgs.append(sending_msgs)
    
    return msgs, sent_msgs

old, new = send_msgs(msgs, sent_msgs)

print("Below msgs are sent: ")
for msg in new:
    print(msg)
    
print(old)