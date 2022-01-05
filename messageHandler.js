// https://github.com/itschandra02/radja-bot

const fs = require("fs");
const axios = require("axios");
const PDFDocument = require("pdfkit");
const brainly = require("brainly-scraper");
const tesseract = require("node-tesseract-ocr");
const webpConverter = require("./lib/webpconverter.js")
const bahasa_planet = require('./lib/bahasa_planet')
const WSF = require("wa-sticker-formatter");
const { MessageType, Mimetype } = require("@adiwajshing/baileys");
const inPdfInput = [];
const questionAnswer = {};
const bufferImagesForPdf = {};
const quotesList = JSON.parse(fs.readFileSync("lib/quotes.json", "utf-8"));
const factList = JSON.parse(fs.readFileSync("lib/fact.json", "utf-8"));
module.exports = async (conn, message) => {
	const senderNumber = message.key.remoteJid;
	const imageMessage = message.message.imageMessage;
	const videoMessage = message.message.videoMessage;
	const stickerMessage = message.message.stickerMessage;
	const extendedTextMessage = message.message.extendedTextMessage;
	const quotedMessageContext = extendedTextMessage && extendedTextMessage.contextInfo && extendedTextMessage.contextInfo;
	const quotedMessage = quotedMessageContext && quotedMessageContext.quotedMessage;
	const textMessage = message.message.conversation || message.message.extendedTextMessage && message.message.extendedTextMessage.text || imageMessage && imageMessage.caption || videoMessage && videoMessage.caption
	let command, parameter;
	if (textMessage) {
		// command = textMessage.trim().split(" ")[0];
		// parameter = textMessage.trim().split(" ").slice(1).join(" ");

		let a = textMessage.trim().split("\n");
		let b = "";
		command = a[0].split(" ")[0];
		b += a[0].split(" ").slice(1).join(" ");
		b += a.slice(1).join("\n")
		parameter = b.trim();
	}

	if (inPdfInput.includes(senderNumber)) {
		if (stickerMessage) return;
		if (command == "!done" || bufferImagesForPdf[senderNumber].length > 19) {
			const pdf = new PDFDocument({ autoFirstPage:false });
			const bufferImages = bufferImagesForPdf[senderNumber];
			for (const bufferImage of bufferImages) {
				const image = pdf.openImage(bufferImage);
				pdf.addPage({ size:[image.width, image.height] });
				pdf.image(image, 0, 0);
			}

			const pathFile = ".temp/" + Math.floor(Math.random() * 1000000 + 1) + ".pdf";
			const file = fs.createWriteStream(pathFile);
			pdf.pipe(file)
			pdf.end()

			file.on("finish", () => {
				const file = fs.readFileSync(pathFile);
				conn.sendMessage(senderNumber, file, MessageType.document, { mimetype: Mimetype.pdf, filename: Math.floor(Math.random() * 1000000) + ".pdf", quoted: message});
				fs.unlinkSync(pathFile);
				inPdfInput.splice(inPdfInput.indexOf(senderNumber), 1);
				delete bufferImagesForPdf[senderNumber];
			})

		} else if (command == "!cancel") {
			delete bufferImagesForPdf[senderNumber];
			inPdfInput.splice(inPdfInput.indexOf(senderNumber), 1);
			conn.sendMessage(senderNumber, "𝙾𝚙𝚎𝚛𝚊𝚜𝚒 𝚍𝚒𝚋𝚊𝚝𝚊𝚕𝚔𝚊𝚗!", MessageType.text, { quoted: message })

		} else if (imageMessage && imageMessage.mimetype == "image/jpeg") {
			const bufferImage = await conn.downloadMediaMessage(message);
			bufferImagesForPdf[senderNumber].push(bufferImage);

			conn.sendMessage(senderNumber, `[${bufferImagesForPdf[senderNumber].length}] 𝙱𝚎𝚛𝚑𝚊𝚜𝚒𝚕 𝚖𝚎𝚗𝚊𝚖𝚋𝚊𝚑𝚔𝚊𝚗 𝚐𝚊𝚖𝚋𝚊𝚛!, 𝚔𝚒𝚛𝚒𝚖 *!𝚍𝚘𝚗𝚎* 𝚓𝚒𝚔𝚊 𝚜𝚎𝚕𝚎𝚜𝚊𝚒, *!𝚌𝚊𝚗𝚌𝚎𝚕* 𝚒𝚗𝚐𝚒𝚗 𝚖𝚎𝚖𝚋𝚊𝚝𝚊𝚕𝚔𝚊𝚗`, MessageType.text, { quoted: message })
			
		} else {
			conn.sendMessage(senderNumber, "𝚒𝚝𝚞 𝚋𝚞𝚔𝚊𝚗 𝚐𝚊𝚖𝚋𝚊𝚛 𝚜𝚊𝚢𝚊𝚗𝚐! 𝚔𝚒𝚛𝚒𝚖 *!𝚍𝚘𝚗𝚜* 𝚓𝚒𝚔𝚊 𝚜𝚎𝚕𝚎𝚜𝚊𝚒, *!cancel* 𝚓𝚒𝚔𝚊 𝚒𝚗𝚐𝚒𝚗 𝚖𝚎𝚖𝚋𝚊𝚝𝚊𝚕𝚔𝚊𝚗", MessageType.text, { quoted: message })
		}

		return;
	}

	switch (command) {
		case "!help":
		case "!menu":
		{
const text =
`「 ❏ 𝗜𝗡𝗙𝗢 𝗕𝗢𝗧 」
ꔹ 𝑵𝒂𝒎𝒂 : *${conn.user.name}*!
ꔹ 𝑶𝒘𝒏𝒆𝒓 : Radja Aditya Chandra
ꔹ 𝑴𝒐𝒅𝒆 : SELF BOT

「 ❏ 𝗜𝗡𝗙𝗢 𝗔𝗨𝗧𝗛𝗢𝗥 」
ꔹ 𝑨𝒖𝒕𝒉𝒐𝒓 : Radja Aditya Chandra
ꔹ 𝑵𝒐𝒎𝒐𝒓 : wa.me/6281262163214
ꔹ 𝑾𝒆𝒃𝒔𝒊𝒕𝒆 : https://www.indocan.asia
ꔹ 𝑰𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎: @itschandra_28

━━━━━━━━━━━━━━━━━━━━━━
━━━━━「 𝑨𝑳𝑳 𝑴𝑬𝑵𝑼 」━━━━━
━━━━━━━━━━━━━━━━━━━━━━

● !menu
● !bantuan
● !sticker <reply image>
● !contact 
● !stickernobg {erorr}
● !pdf 
● !toimg
● !togif
● !gifsticker
● !textsticker {erorr}
● !giftextsticker
● !write
● !brainly
● !quotes
● !randomfact
● !gtts [kode bahasa] [text]
● !wikipedia [query]
● !math
● !donasi
● !bplanet
● !ocr
● !info`

			conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
			break;
		}

        case "!bantuan":
    {    
            const text = `kirim *!help/!menu* untuk melihat daftar perintah dari bot ini

- kirim *!contact* untuk menghubungi pembuat bot

- kirim gambar dengan caption *!sticker* untuk membuat sticker

- kirim gambar dengan caption *!stickernobg* untuk membuat sticker tanpa background

- kirim *!pdf* untuk membuat pdf dari gambar

- reply sticker dengan caption *!toimg* untuk membuat sticker ke gambar

- reply sticker bergerak dengan caption *!togif* untuk membuat sticker ke gif

- kirim *!textsticker [text kamu]* untuk membuat text sticker
  contoh: !textsticker ini sticker

- kirim *!giftextsticker [text kamu]* untuk membuat text sticker jedag jedug
  contoh: !giftextsticker ini sticker

- kirim video dengan caption *!gifsticker* untuk membuat sticker bergerak

- kirim *!write [masukan text disini]* untuk menulis ke kertas
  contoh: !write ini tulisanku

- kirim *!brainly [pertanyaan kamu]* untuk mencari pertanyaan dan jawaban di brainly
  contoh: !brainly apa itu nodejs

- *!quotes* untuk mendapatkan quotes

- *!randomfact* untuk mendapatkan pengetahuan acak

- *!gtts [kode bahasa] [text]* untuk mengubah text ke suara google. Untuk kode bahasa dilihat disini https://s.id/xSj1g
   contoh: !gtts id saya bot

- *!wikipedia [query]* untuk mencari dan membaca artikel di wikipedia
   contoh: !wikipedia Python

- *!math* untuk mengerjakan soal matematika 

- *!bplanet [alias] [text]*
   contoh: !bplanet g kamu lagi ngapain?

- kirim gambar dengan caption *!ocr* untuk mendapatkan text dari gambar`;

            conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
			break;
		}
		
		case "!donasi":
        case "!donate":
{
const text =`Hallo, kak bantu donasi nya dong 👋
╭──❉ *DONASI KAK* ❉─────
│➸ *DANA*: 081262163214
│➸ *PULSA*: 081262163214
│➸ *GOPAY*: 081262163214
│➸ *OVO*: 081262163214
╰──────────────────
╭─────────────────
│  ▌│█║▌║▌║║▌║▌║█│▌
│  ▌│█║▌║▌║║▌║▌║█│▌
│
│ _*POWERED BY ITSCHADRA*_
╰──────────────────`
 conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
			break;
	    }
	        case "!rules":
	        case "!peraturan":
	  {      
	        const text =`*「 PERATURAN BOT 」*

1. DILARANG TELFON BOT!!
2. DILARANG SPAM BOT
3. DILARANG BERKATA KASAR
4. DILARANG SPAM VIRTEX
5. DILARANG TELEFON OWNER
6. DILARANG SPAM GROUP
7. DILARANG SPAM ADMIN
8. DILARANG BERKATA KASAR DI GC

⚠️JIKA KALIAN MELANGGAR.. AKAN DI BLOCK + BANNED!!`
conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
            break;
          }
			case "!contact":
		{
			const text = `Hubungi saya di

- Facebook: fb.me/salismazaya
- Telegram: t.me/salismiftah
- Email: salismazaya@gmail.com`;
			conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
			break;
		}

		case "!sticker":
		case "!stiker":
		{
			if (quotedMessage) {
				message.message = quotedMessage;
			}

			if (!message.message.imageMessage || message.message.imageMessage.mimetype != "image/jpeg") {
				conn.sendMessage(senderNumber, "Tidak ada gambar :)", MessageType.text, { quoted: message });
				break;
			}

			const imagePath = await conn.downloadAndSaveMediaMessage(message, Math.floor(Math.random() * 1000000));
			const sticker = new WSF.Sticker("./" + imagePath, { crop: false, pack: "𝚒𝚝𝚜𝚌𝚑𝚊𝚗𝚍𝚛𝚊 :)", author: '@𝚒𝚝𝚜𝚌𝚑𝚊𝚗𝚍𝚛𝚊_28' });
			await sticker.build();
			fs.unlinkSync(imagePath);
			const bufferImage = await sticker.get();
			conn.sendMessage(senderNumber, bufferImage, MessageType.sticker, { quoted: message });
			break;
		}

		case "!toimg":
		{
			if (!quotedMessage || !quotedMessage.stickerMessage || quotedMessage.stickerMessage.mimetype != "image/webp") {
				conn.sendMessage(senderNumber, "Harus me-reply sticker :)", MessageType.text, { quoted: message });
				break;
			}

			message.message = quotedMessage;
			const webpImage = await conn.downloadMediaMessage(message);
			const jpgImage = await webpConverter.webpToJpg(webpImage);
			conn.sendMessage(senderNumber, jpgImage, MessageType.image, { quoted: message, caption: "Ini gambarnya kak!" });
			break;
		}

		
		case "!togif":
		{
			if (!quotedMessage || !quotedMessage.stickerMessage || quotedMessage.stickerMessage.mimetype != "image/webp") {
				conn.sendMessage(senderNumber, "Harus me-reply sticker :)", MessageType.text, { quoted: message });
				break;
			}

			message.message = quotedMessage;
			const webpImage = await conn.downloadMediaMessage(message);
			const video = await webpConverter.webpToVideo(webpImage);
			conn.sendMessage(senderNumber, video, MessageType.video, { quoted: message, mimetype: Mimetype.gif });
			break;
		}

		case "!write":
		case "!nulis":
		{
			if (!parameter) {
				conn.sendMessage(senderNumber, "Tidak ada text :)", MessageType.text, { quoted: message });
				break;
			}

			const response = await axios.post("https://salism3api.pythonanywhere.com/write", { "text": parameter });
			const imagesUrl = response.data.images.slice(0, 4);

			for (const imageUrl of imagesUrl) {
				const response = await axios({
					url: imageUrl,
					method: "GET",
					responseType: "arraybuffer",
				});
				const image = Buffer.from(response.data, "binary");
				await conn.sendMessage(senderNumber, image, MessageType.image, { quoted: message });
			}
			break;
		}

		case "!pdf":
		{
			if (message.participant) {
				conn.sendMessage(senderNumber, "Fitur ini tidak bisa berjalan di grup :(", MessageType.text, { quoted: message });
				break;
			}

			if (imageMessage) {
				conn.sendMessage(senderNumber, "Kirim tanpa gambar!", MessageType.text, { quoted: message });
				break;
			}

			inPdfInput.push(senderNumber);
			bufferImagesForPdf[senderNumber] = [];

			conn.sendMessage(senderNumber, "Silahkan kirim gambarnya satu persatu! jangan spam ya!", MessageType.text, { quoted: message });
			break;
		}

		case "!brainly":
		{
			if (!parameter) {
				conn.sendMessage(senderNumber, "Inputnya salah kak :)", MessageType.text, { quoted: message });
				break;
			}

			const data = await brainly(parameter);
			if (data.succses && data.data.length <= 0) {
				conn.sendMessage(senderNumber, "Pertanyaan tidak ditemukan :(", MessageType.text, { quoted: message })

			} else if (data.success) {
				for (const question of data.data.slice(0, 3)) {
					const text = `*Pertanyaan:* ${question.pertanyaan.trim()}\n\n*Jawaban*: ${question.jawaban[0].text.replace("Jawaban:", "").trim()}`
					await conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message })
				}
			}
			break;
		}

		case "!quotes":
		{
			const quotes = quotesList[Math.floor(Math.random() * quotesList.length)];
			const text = `_"${quotes.quote}"_\n\n - ${quotes.by}`;
			conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
			break;
		}

		case "!randomfact":
		case "!fact":
		{
			const fact = factList[Math.floor(Math.random() * factList.length)];
			const text = `_${fact}_`
			conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
			break;
		}

		case "!gtts":
		case "!tts":
		case "!text2sound":
		{
			if (!parameter) {
				conn.sendMessage(senderNumber, "Inputnya salah kak :)", MessageType.text, { quoted: message });
				break;
			}

			if (parameter.split(" ").length == 1) {
				conn.sendMessage(senderNumber, "Tidak ada kode bahasa / teks", MessageType.text, { quoted: message });
				break;
			}

			const language = parameter.split(" ")[0];
			const text = parameter.split(" ").splice(1).join(" ");
			axios({
				url: `https://salism3api.pythonanywhere.com/text2sound`,
				method: "POST",
				responseType: "arraybuffer",
				data: {
					"languageCode": language,
					"text": text,
				}
			}).then(response => {
				const audio = Buffer.from(response.data, "binary");
				conn.sendMessage(senderNumber, audio, MessageType.audio, { ptt: true, quoted: message });

			}).catch(response => {
				conn.sendMessage(senderNumber, `Kode bahasa *${language}* tidak ditemukan :(`, MessageType.text, { quoted: message });

			});
			break;
		}

		case "!wikipedia":
		case "!wiki":
		{
			if (!parameter) {
				conn.sendMessage(senderNumber, "Inputnya salah kak :)", MessageType.text, { quoted: message });
				break;
			}

			axios.post("http://salism3api.pythonanywhere.com/wikipedia", { "query":parameter })
				.then(response => {
					const text = `*${response.data.title}*\n\n${response.data.content}`;
					conn.sendMessage(senderNumber, text, MessageType.text, { quoted: message });
				})
				.catch(e => {
					if ([ 500, 400, 404 ].includes(e.response.status)) {
						conn.sendMessage(senderNumber, `Artikel tidak ditemukan :(`, MessageType.text, { quoted: message });
					} else {
						throw e;
					}
				})
			break;
		}

		case "!textsticker":
		case "!textstiker":
		{
			if (!parameter) {
				conn.sendMessage(senderNumber, "Inputnya salah kak :)", MessageType.text, { quoted: message });
				break;
			}

			const response = await axios.post("https://salism3api.pythonanywhere.com/text2img", { "text":parameter.slice(0,60) });
			const sticker = new WSF.Sticker(response.data.image, { crop: false, pack: "itschandra", author: '@itschandra_28' });
			await sticker.build();
			const bufferImage = await sticker.get();
			conn.sendMessage(senderNumber, bufferImage, MessageType.sticker, { quoted: message });
			break;
		}

		case "!ocr":
		{
			if (quotedMessage) {
				message.message = quotedMessage;
			}

			if (!message.message.imageMessage || message.message.imageMessage.mimetype != "image/jpeg") {
				conn.sendMessage(senderNumber, "Tidak ada gambar :)", MessageType.text, { quoted: message });
				break;
			}
			const imagePath = await conn.downloadAndSaveMediaMessage(message, Math.floor(Math.random() * 1000000));
			const textImage = (await tesseract.recognize(imagePath)).trim();
			fs.unlinkSync(imagePath)

			conn.sendMessage(senderNumber, textImage, MessageType.text, { quoted: message });		
			break;
		}

		case "!gifsticker":
		{
			if (quotedMessage) {
				message.message = quotedMessage;
			}

			if (!message.message.videoMessage || message.message.videoMessage.mimetype != "video/mp4") {
				conn.sendMessage(senderNumber, "Tidak ada video :)", MessageType.text, { quoted: message });
				break;
			}

			if (message.message.videoMessage.seconds > 30) {
				conn.sendMessage(senderNumber, "Maksimal 30 detik!", MessageType.text, { quoted: message });
				break;	
			}

			const imagePath = await conn.downloadAndSaveMediaMessage(message, Math.floor(Math.random() * 1000000));
			const sticker = new WSF.Sticker("./" + imagePath, { animated: true, pack: "i hope you fine :)", author: 'Sugito Tempest' });
			await sticker.build();
			fs.unlinkSync(imagePath);
			const bufferImage = await sticker.get();
			conn.sendMessage(senderNumber, bufferImage, MessageType.sticker, { quoted: message });
			break;
		}

		case "!giftextsticker":
		{
			if (!parameter) {
				conn.sendMessage(senderNumber, "Inputnya salah kak :)", MessageType.text, { quoted: message });
				break;
			}

			const response = await axios.post("https://salism3api.pythonanywhere.com/text2gif/", { "text":parameter.slice(0,60) });
			let image = await axios.get(response.data.image, { "responseType":"arraybuffer" });
			image = Buffer.from(image.data, "binary");
			image = await webpConverter.gifToWebp(image);
			conn.sendMessage(senderNumber, image, MessageType.sticker, { quoted: message });
			break;	
		}


		case "!math":
		{
			const response = await axios.get("https://salism3api.pythonanywhere.com/math/");
			let image = await axios.get(response.data.image, { "responseType":"arraybuffer" });
			image = Buffer.from(image.data, "binary");
			const msg = await conn.sendMessage(senderNumber, image, MessageType.image, { quoted: message, caption: "Balas pesan ini untuk menjawab!"});
			questionAnswer[msg.key.id] = response.data.answer;

			setTimeout(() => {
				if (questionAnswer[msg.key.id]) {
					conn.sendMessage(senderNumber, "Waktu habis!", MessageType.text, { quoted: msg });
					delete questionAnswer[msg.key.id];
				}
			}, 600 * 1000);
			break;
		}

		case "!stickernobg":
		case "!stikernobg":
		case "!snobg":
		{
			if (quotedMessage) {
				message.message = quotedMessage;
			}

			if (!message.message.imageMessage || message.message.imageMessage.mimetype != "image/jpeg") {
				conn.sendMessage(senderNumber, "Tidak ada gambar :)", MessageType.text, { quoted: message });
				break;
			}

			const image = await conn.downloadMediaMessage(message);
			const imageb64 = image.toString('base64')
			conn.sendMessage(senderNumber, 'Tunggu ya kak!', MessageType.text);
			const data = await axios.post('https://salisganteng.pythonanywhere.com/api/remove-bg', {
				'api-key': 'salisheker',
				'image': imageb64,
			})

			const sticker = new WSF.Sticker(data.data.image, { crop: false, pack: "i hope you fine :)", author: 'Sugito Tempest' });
			await sticker.build();
			const bufferImage = await sticker.get();
			conn.sendMessage(senderNumber, bufferImage, MessageType.sticker, { quoted: message });
			break;
		}

                /**
                 * Konversi bahasa planet
                 * use: !bplanet g kamu lagi ngapain
                 * result: kagamugu lagagigi ngagapagaigin
                 **/
                case '!bplanet':
                    if (quotedMessage) message.message = quotedMessage
                    if (!!parameter) {
                        var [ alias, ...text ] = parameter.split` `
                        text = text.join` `
                        conn['sendMessage'](senderNumber, bahasa_planet(text, alias), 'conversation', {
                            quoted: message
                        })
                    } else {
                        var contoh = '[wrong format]\n\nformat: !bplanet <alias> <text>\ncontoh: !bplanet g kamu lagi ngapain?'
                        conn['sendMessage'](senderNumber, contoh, 'conversation', {
                            quoted: message
                        })
                    }
                    break
		default:
		{
			if (quotedMessage && questionAnswer[quotedMessageContext.stanzaId] && textMessage) {
				const answer = questionAnswer[quotedMessageContext.stanzaId];
				if (answer == parseInt(textMessage)) {
					conn.sendMessage(senderNumber, "Keren! jawaban benar", MessageType.text, { quoted: message });
					delete questionAnswer[quotedMessageContext.stanzaId];
				} else {
					conn.sendMessage(senderNumber, "Jawaban salah!", MessageType.text, { quoted: message })
				}
			} else if (!message.participant && !stickerMessage) {
				conn.sendMessage(senderNumber, "Command tidak terdaftar, kirim *!help* untuk melihat command terdaftar", MessageType.text, { quoted: message });
			}
		}

	}
}
