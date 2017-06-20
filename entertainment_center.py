#importing class file named media.py
import media

#importing fresh_tomatoes.py

import fresh_tomatoes

#creating instances of class websiteproject

Mahesh = media.Movies("Maheshinte Prathikaram",
"Mahesh, a photographer, gets beaten up by a stranger when he tries to solve an issue in his village. He sets out to take revenge on the stranger as he feels insulted after the incident.",
"http://www.cochintalkies.com/movie/poster/10/maheshinte-prathikaram-movie-poster-9168.jpg",
"https://www.youtube.com/watch?v=_KY8Du4WWew")

Take_off  = media.Movies("Take OFF",
"A young Muslim woman (Parvathy) struggles to find love and happiness in midst of the ongoing civil war in Iraq.",
"http://img.nowrunning.com/content/movie/2017/take-20113/stills/takeoff-cinema-photos08.jpg",
"https://www.youtube.com/watch?v=B2DGTD1Heg4")

Twenty_four = media.Movies("24",
"Sethuraman, a scientist, invents a time-travelling gadget, and his evil-twin brother wants to get hold of it. A bitter battle arises between Sethuraman's son and his evil-twin to capture the gadget.",
"http://www.india.com/wp-content/uploads/2016/04/re3.jpg",
"https://www.youtube.com/watch?v=tBkngXt7LLs")

bahubali_1 = media.Movies("BAHUBALI",
"Shiva, the son of Bahubali, begins to search for answers after he learns about his heritage.",
"https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
"https://www.youtube.com/watch?v=sOEg_YZQsTI")

bahubali_2 = media.Movies("BAHUBALI 2",
"After vanquishing the Kalakeyas, Amarendra Baahubali is declared as the future king of Mahishmati and Bhallaladeva (Rana Daggubati) is declared as the commander-in-chief. Before the coronation, Rajamatha Sivagami (Ramya Krishnan) begins to look for a bride for Amarendra. She instructs Amarendra and Kattappa to tour the kingdom to understand its current state and its people.",
"http://stat2.bollywoodhungama.in/wp-content/uploads/2017/01/Bahubali-2-The-Conclusion-4.jpg",
"https://www.youtube.com/watch?v=94BzBOpv42g")

I_movie = media.Movies(" I ",
"Lingesan (Vikram) is a bodybuilder from Chennai, whose main ambition is to become Mr. India. He wins the title of Mr. Tamil Nadu, which gives him direct entry to the Mr. India pageant. He is infatuated by Diya (Amy Jackson), a leading supermodel. Diya is soon blacklisted, with all her advertisement film contracts cancelled by John (Upen Patel), her co-star in all her advertisements, after she constantly rejected his advances. To save her career, Diya decides to replace John with Lingesan, whom she had earlier met at one of her shoots, as her co-star for her next advertisement. The shooting is to take place in China at the same time when the Mr. India paegant is to take place, but Lingesan agrees, sacrificing his Mr. India ambitions in the process.",
"https://upload.wikimedia.org/wikipedia/en/5/56/I_film_poster.jpg",
"https://www.youtube.com/watch?v=8uPK9Ov6Zd4")

Druvam = media.Movies("Dhruva Natchathiram",
"Dhruva Natchathiram is an upcoming Tamil-language action spy thriller film produced, written and directed by Gautham Menon. Featuring Vikram in the lead role, the film began production in January 2017. ",
"https://upload.wikimedia.org/wikipedia/en/thumb/2/20/Dhruva_Natchathiram_poster.jpg/220px-Dhruva_Natchathiram_poster.jpg",
"https://www.youtube.com/watch?v=Jfyjx2rOQWk")

rocky = media.Movies("rocky",
"if you use single underscores, you merely create a method named _init_, and get a default constructor, which takes no arguments.",
"http://t3.gstatic.com/images?q=tbn:ANd9GcT2p31vnqkRv-SOj-5NfYVKS7a0ge6XvQU0QTCSPiLKdQhxizvx",
"https://www.youtube.com/watch?v=mMjPokU5-0w"
)

Iru_mugan = media.Movies("Iru Mugan",
"Following the attack on the Indian Embassy in Malaysia, Akhilan, an ex-agent, is assigned to track down the culprit. His investigations lead him to his old foe who has now developed a hazardous drug",
"http://t0.gstatic.com/images?q=tbn:ANd9GcQpYy-rJQyXLG2rR2cUs7Rk__3wyEG3abaPaCQEI-FSY3skvpFl",
"https://www.youtube.com/watch?v=L_0jexAQsB0")

charlie = media.Movies("charlie",
"Tessa runs away from home to avoid getting married and rents a room. She finds a sketchbook of the previous occupant, which reveals an incomplete story and decides to find this man.",
"https://upload.wikimedia.org/wikipedia/en/4/4e/Charlie_2015-Malayalam_film_poster.jpg",
"https://www.youtube.com/watch?v=Sz_HiHXcPDg")

Brothers = media.Movies("Brothers",
"Destiny brings two estranged brothers, David and Monty, face-to-face as they fight it out against each other in a mixed martial arts tournament and settle scores of the past.",
"http://t3.gstatic.com/images?q=tbn:ANd9GcT7W4qAYJ1gVEEA50j2E9o8P1YGqugkSlBvhCX-RHQNWbeoaExU",
"https://www.youtube.com/watch?v=QuRSCU0tOKs")

dhoni = media.Movies("M.S.Dhoni - The Untold Story",
"Ranchi lad M S Dhoni aspires to play cricket for India. Though he initially tries to please his father by taking up a job with the Indian Railways, he ultimately decides to chase his dreams.",
"http://t0.gstatic.com/images?q=tbn:ANd9GcSbgMguXb4cBUMBEdZkYA_CpjHWHQQpPPNrMnBvp5PDeXiMedL-",
"https://www.youtube.com/watch?v=6L6XqWoS8tw")



#creating an array of movie names used to pass into the function called open_movies_page()
movies = [Mahesh,Take_off,Twenty_four,bahubali_1,bahubali_2,I_movie,Druvam,rocky,Iru_mugan,charlie,Brothers,dhoni]


#calling function open_movies_page with movies array as argument passing
fresh_tomatoes.open_movies_page(movies)
