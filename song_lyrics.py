import time

lyrics = [
    (0, "Baby, I'm fallin', losin' my focus"),
    (5, "How come you're actin' like you haven't noticed?"),
    (10, "I'm going crazy, stuck with your maybe"),
    (15, "Left me in nowhere, my beautiful nightmare"),
    (20, "Oh, my love"),
    (23, "When I look into your eyes"),
    (26, "Girl, it gets me everytime"),
    (29, "And I thought that you should know"),
    (33, "(Oh-oh-oh)"),
    (36, "That I got you on my mind, on my mind, on my mind"),
    (41, "I want you all the time, all the time, every night"),
    (46, "Tell me you feel it too"),
    (49, "You don't have to play it cool"),
    (52, "'Cause I got you on my mind, on my mind, on my mind"),
    (58, "Cool as a cold war, hot like a fever"),
    (62, "I'm tryna hold on, 'cause, baby, I need ya"),
    (67, "You're so contagious, tell me I'll make it"),
    (72, "Act like you don't know, I'm calling your Limbo"),
    (77, "Oh, my love..."),
    (82, "When I look into your eyes"),
    (85, "Girl, it gets me everytime"),
    (88, "And I thought that you should know"),
    (91, "(Oh-oh-oh)"),
    (94, "That I got you on my mind, on my mind, on my mind"),
    (99, "I want you all the time, all the time, every night"),
    (104, "Tell me you feel it too"),
    (107, "You don't have to play it cool"),
    (110, "'Cause I got you on my mind, on my mind, on my mind"),
    (116, "Come on, baby, get closer..."),
    (130, "On my mind, on my mind (fade out...)")
]

start_time = time.time()
for t, text in lyrics:
    while time.time() - start_time < t:
        time.sleep(0.1)
    print(text)
