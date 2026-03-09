msgs = ["Hello", "Hi", "Namaste", "Bonjour!", "Sastriyakal"]
sent_msgs = []

def send_msgs(msgs, sent_msgs):
    """function to show messages"""
    while msgs:
        sending_msg = msgs.pop()
        print(f"Currently sending, {sending_msg}")
        sent_msgs.append(sending_msg)

    return msgs, sent_msgs

    
o_msgs, n_msgs = send_msgs(msgs[:], sent_msgs)
print(msgs)
print(o_msgs)
print(n_msgs)