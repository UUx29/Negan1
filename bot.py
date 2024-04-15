<?php
ob_start();
$token = "7184086344:AAHjrClAUZJuPHtosjczCzJzshcx4ZMPbv0";
define("API_KEY", $token);

function bot($method, $datas = [])
{
    $sswwp = http_build_query($datas);
    $url = "https://api.telegram.org/bot" . API_KEY . "/" . $method . "?$sswwp";
    $sswwp = file_get_contents($url);
    return json_decode($sswwp);
}

$update = json_decode(file_get_contents('php://input'));

@$message = $update->message;
@$from_id = $message->from->id;
@$chat_id = $message->chat->id;
@$message_id = $message->message_id;
@$first_name = $message->from->first_name;
@$last_name = $message->from->last_name;
@$username = $message->from->username;
@$text = $message->text;
@$firstname = $update->callback_query->from->first_name;
@$usernames = $update->callback_query->from->username;
@$chatid = $update->callback_query->message->chat->id;
@$fromid = $update->callback_query->from->id;
$message = $update->message;
$from_id = $update->callback_query->from->id;
$from_id = $message->from->id;
$name = $message->from->first_name;

if (isset($update->callback_query)) {
    $up = $update->callback_query;
    $chat_id = $up->message->chat->id;
    $from_id = $up->from->id;
    $user = $up->from->username;
    $text = $up->message->text;
    $name = $up->from->first_name;
    $message_id = $up->message->message_id;
    $data = $up->data;
}

$BotDatabase = json_decode(file_get_contents("DataBaseBot.json"), 1);

if ($text == "/start") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "أهلا بك عزيزي $name في بوتنا الرسمي 🎬🤍

نقدم لكم المسلسلات والأفلام نتمنى إن ينال على إعجابك 📽️🤍

يحتوي البوت على مسلسلات تركية وأفلام عربية والخ...☑️",
        'parse_mode' => "markdown",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'المسلسلات 🎬'], ['text' => 'الأفلام 🎞️']],
                [['text' => 'الطلبات 🛎'], ['text' => 'بحث 📽️']],
                [['text' => 'تقيم البوت🤖'], ['text' => 'قناة البوت 🏹']],
                [['text' => 'مبرمجين البوت 🤍']],
            ],
            'resize_keyboard' => true,
            'one_time_keyboard' => false,
            'selective' => false,
        ]),
    ]);
}

if ($text == "رجوع") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "أهلا بك عزيزي $name في بوتنا الرسمي 🎬🤍

نقدم لكم المسلسلات والأفلام نتمنى إن ينال على إعجابك 📽️🤍

يحتوي البوت على مسلسلات تركية وأفلام عربية والخ...☑️",
        'parse_mode' => "markdown",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'المسلسلات 🎬'], ['text' => 'الأفلام 🎞️']],
                [['text' => 'الطلبات 🛎'], ['text' => 'بحث 📽️']],
                [['text' => 'تقيم البوت🤖'], ['text' => 'قناة البوت 🏹']],
                [['text' => 'مبرمجين البوت 🤍']],
            ],
            'resize_keyboard' => true,
            'one_time_keyboard' => false,
            'selective' => false,
        ]),
    ]);
}


if ($data == "rj") {
    bot('editMessageText', [
        'chat_id' => $chat_id,
        'message_id' => $message_id,
        'text' => "أهلا بك عزيزي $name في بوتنا الرسمي 🎬🤍

نقدم لكم المسلسلات والأفلام نتمنى إن ينال على إعجابك 📽️🤍

يحتوي البوت على مسلسلات تركية وأفلام عربية والخ...☑️",
'parse_mode' => "markdown",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'المسلسلات 🎬'], ['text' => 'الأفلام 🎞️']],
                [['text' => 'الطلبات 🛎'], ['text' => 'بحث 📽️']],
                [['text' => 'تقيم البوت🤖'], ['text' => 'قناة البوت 🏹']],
                [['text' => 'مبرمجين البوت 🤍']],
            ],
            'resize_keyboard' => true,
            'one_time_keyboard' => false,
            'selective' => false,
        ]),
    ]);
}



if ($text == "المسلسلات 🎬") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختر مسلسلتك؟",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'مسلسل اخوتي🇹🇷'], ['text' => 'مسلسل اسكندر العاصف🇹🇷']],
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}

if ($text == "مسلسل اخوتي🇹🇷") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختر الحلقة",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => '114'], ['text' => '115']],
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}




if ($text == "114") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/5",
        "caption" => "‹ حلقة رقم 114 ›",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}



if ($text == "115") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/6",
        "caption" => "‹ حلقة رقم 115 ›",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}


if ($text == "مسلسل اسكندر العاصف🇹🇷") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختر الحلقة",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => '1'], ['text' => '2']],
                [['text' => '3'], ['text' => '4']],
                [['text' => '5'], ['text' => '6']],
                [['text' => '7'], ['text' => '8']],
                [['text' => '9'], ['text' => '10']],
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}




if ($text == "1") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/7",
        "caption" => "حلقة 1",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "2") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/8",
        "caption" => "حلقة 2",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "3") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/9",
        "caption" => "حلقة 3",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "4") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/10",
        "caption" => "حلقة 4",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/sjadiraqi"]],
            ],
        ]),
    ]);
}

       
   
if ($text == "5") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/10",
        "caption" => "حلقة 5",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "6") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/12",
        "caption" => "حلقة 6",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
 if ($text == "7") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/13",
        "caption" => "حلقة 7",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "8") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/14",
        "caption" => "حلقة 8",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "9") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/15",
        "caption" => "حلقة 9",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
if ($text == "10") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/16",
        "caption" => "حلقة 10",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}

       
       
if ($text == "الأفلام 🎞️") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختر النوع",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'افلام عربية 🟢'], ['text' => 'افلام اجنبية ⚪']],
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}

if ($text == "افلام عربية 🟢") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختر الفلم",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'فلم تاج 🟢'], ['text' => 'فلم فضل ونعمة 🟢']],
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}




if ($text == "فلم تاج 🟢") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/17",
        "caption" => "فلم تاج🟢",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}


if ($text == "فلم فضل ونعمة 🟢") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/18",
        "caption" => "فلم فضل ونعمة 🟢",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}



if ($text == "افلام اجنبية ⚪") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "اختر الفلم",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'فلم باربي⚪'], ['text' => 'فلم اوبنهايمر⚪']],
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}



if ($text == "فلم اوبنهايمر⚪") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/22",
        "caption" => "فـيـلـم اوبـنهـايـمـر - جودة عالية (1080p) مـترجـم",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}


if ($text == "فلم باربي⚪") {
    bot("sendvideo", [
        "chat_id" => $chat_id,
        "video" => "https://t.me/sosisoap/23",
        "caption" => "فيلم باربي - مترجم كامل!

• الجودة = 1080p

-",
        'reply_to_message_id' => $message->message_id,
        "reply_markup" => json_encode([
            "inline_keyboard" => [
                [["text" => "المطور 🏹", "url" => "https://t.me/L1_Y2"]],
            ],
        ]),
    ]);
}



if ($text == "الطلبات 🛎") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'message_id' => $message_id,
        'text' => "الطلبات 🔥",
        'disable_web_page_preview' => true,
        'parse_mode' => "markdown",
        'reply_markup' => json_encode([
            'inline_keyboard' => [
                [['text' => 'سفاح الجيزه', 'callback_data' => "tt"]],
                [['text' => 'مسلسل طائر الرفراف', 'callback_data' => "tt"]],
                [['text' => 'أميرة بلا تاج', 'callback_data' => "tt"]],
                [['text' => 'غسيل', 'callback_data' => "tt"]],
                [['text' => 'المعلم', 'callback_data' => "tt"]],
                [['text' => 'بن تن', 'callback_data' => "tt"]],
            ]
        ])
    ]);
}



if ($text == "بحث 📽️") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "هذا القسم مقفول حالياً 🎬",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}


if ($text == "تقيم البوت🤖") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'message_id' => $message_id,
        'text' => "ما تقيمك للبوت",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'مو حلو😡']],
                [['text' => 'لا بأس🫥']],
                [['text' => 'حلو😀']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}

if ($text == "مو حلو😡") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "~شكرا لتقيمك🤍",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}

if ($text == "لا بأس🫥") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "~شكرا لتقيمك🤍",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}


if ($text == "حلو😀") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "~شكرا لتقيمك🤍",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}

  


  
if ($text == "مبرمجين البوت 🤍") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "تم برمجت هذا البوت بواسطة المبرمج سجاد واسكندر🤍🏹",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}



if ($text == "قناة البوت 🏹") {
    bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => "قناة البوت الرسمية t.me/L1_Y2",
        'reply_markup' => json_encode([
            'keyboard' => [
                [['text' => 'رجوع']],
            ],
            'resize_keyboard' => true,
        ])
    ]);
}

