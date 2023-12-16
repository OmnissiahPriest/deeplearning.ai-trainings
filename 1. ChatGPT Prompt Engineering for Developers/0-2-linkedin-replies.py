from openai import OpenAI
from dotenv import load_dotenv
from redlines import Redlines

load_dotenv()

client = OpenAI()
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

# Prompt1
# message =f"""Hi. I represent CompanyName, A Danish company that specializes in the production and distribution of healthcare and hygiene products.
# # We are looking for Mulesoft talent to take our systems integration initiatives.
# # Would you be interested on learning more about this roles?
# #        warm regards
# #
# #        Headhunter"""

# Prompt2
# message =f"""Dzień dobry,
# 
# jakiś czas temu kontaktowałam się odnośnie propozycji współpracy w obszarze Mulesoft. Pojawiły się nowe projekty.
# 
# Czy obecnie byłby Pan otwarty na zmiany?
# 
# Miłego dnia!
# 
# Headhunter
# HR Specialist
# CompanyName"""
# Prompt3
# message =f"""Platforma CompanyName oparta o Machine Learning - mamy ponad 8 milionów bid requestów na sekundę!
# Cześć Konstyantynie!
# 
# Mam na imię Jagoda, współpracuję bezpośrednio z teamem IT w CompanyName i będąc na Twoim profilu pomyślałam, że może byłbyś zainteresowany rozmową na temat możliwości współpracy z nami - jesteśmy polską firmą o zasięgu globalnym, zajmujemy się prowadzeniem działań retargetingowych :).
# 
# Poszukujemy obecnie CompanyName Integration Engineera - osoby, która będzie pracować przy kodzie (Java), dopasowywać nasz bidder do specyfikacji OpenRTB, mierzyć impakt zmian na performance prowadzonych kampanii, a także kontaktować się z naszymi zewnętrznymi partnerami. Chętnie wykorzystalibyśmy Twoje umiejętności, których dopatrzyłam się na Twoim profilu - chodzi o Javę (Spring), Python i doświadczenie na podobnym stanowisku.
# 
# Nasze miesięczne widełki to 20-25 tys. netto + VAT (B2B), ale do kwestii wynagrodzeń podchodzimy z otwartą głową.
# 
# Jeśli chodzi o tematy organizacyjne: działamy w 100% zdalnie (choć można korzystać z biur w Warszawie i Krakowie) i mamy elastyczny czas pracy. Tu więcej o nas: https://
# 
# Daj znać, czy chciałbyś poznać więcej szczegółów podczas rozmowy telefonicznej. Będę czekać na odpowiedź :).
# 
# Headhunter
# Junior Technical Talent Acquisition Specialist w CompanyName"""
# Prompt4
# message =f"""Hi Kostyantyn ,
# 
# Wish this mail finds you and your family safe and well!
# 
# This is recruiter  from CompanyName, and I am here to support the talent attraction for APM Solutions, which is a joint venture between two industry giants, CompanyName. It aimed at revolutionizing the parcel locker network in Poland.
# 
# APM Solutions is looking for some promising talents for Hardware Technical Engineer based in Warsaw, Poland to join our team for local business expansion.
# -The position is responsible for providing technical support for the installation, operation, maintenance, and troubleshooting of parcel lockers and related hardware products in our company.
# -All the positions we're hiring are required to be on-site and full-time.
# -The office location: CompanyName Warsaw, Poland.
# 
# Let me know if you'd like to discuss the opportunity further, if yes, you can send your CV to me directly, and also I'd like to know your Polish language level.
# If you're not interested but know someone who might be, I'd welcome the recommendation.
# 
# Thanks for your time and attention. Hope this works out.
# 
# Best regards,
# Headhunter"""
# Prompt5
# message =f"""Kostyantyn, hello!
# 
# I'm Headhunter, HR 😇
# I'm really looking for someone with experience in Salesforce manufacturing cloud. Tell me pls, is that you? 🙃"""
# Prompt6
# message =f"""Application Architect Opportunity at CompanyName | Remote Work
# Hi Kostyantyn,
# Greetings for the day!
# I am Headhunter with CompanyName, writing to you in regard to an excellent job opportunity as Application Architect for which you can work Remotely from anywhere in Poland.
# 
# Expectations:
# - Proficiency in Java, Java Servlet, Java JSP, JEE API, 12 Factor Application Design, Spring Boot etc.
# - Frontend: JavaScript, Html, CSS
# - Kubernetes, OpenShift, Cloud experience
# - Experience in deployment of applications to various middleware components & DevOps Framework.
# 
# Since this is an urgent business requirement, I request you to kindly reach out to me by responding to this InMail, or you can email me at .com with your updated CV & I shall get back to you with more relevant details.
# 
# Looking forward to work with you!
# 
# Thank you for your time,
# Headhunter
# Senior Talent Specialist at CompanyName
# """
# Prompt7
# message =f"""Witam serdecznie,
# 
# Jestem rekruterką i specjalizuję się w rekrutacjach branży IT w chwili obecnej prowadzę projekt rekrutacyjny na stanowisko Network& Security Engineera poniżej przesyłam opis stanowiska.
# 
# Your responsibilities
# 
# - In this challenging position, you design the network and security aspects of a station control systems (SCADA) for high and medium voltage switchgears according to the newest technology standards
# - You build up systems related to security standards like IEC62443 and NERC-CIP
# - You implement the planned measures on the devices and the applications Furthermore support the sales organisation during the tender phase and in discussions with the customer
# - With your know-how, you support the project manager in technical matters and coordinate both customers and internal partners
# - Moreover, you prepare procedures and operation manuals that are based on our customer's requirements
# 
# Your background
# 
# - In addition to your degree in power engineering, electrical engineering or information technology, you have experience in station automation, SCADA or process automation
# - You are versed in Cyber Security technology, in networks (LAN) and peripheral devices as well as in the MS Windows environment (MS Server, MS Office)
# - Alongside strong communication skills and team spirit you will have to show the ability to work in an independent manner
# - Good command of English required
# 
# Pracodawca oferuje na tym stanowisku wynagrodzenie zasadnicze do około 160k zł rocznie w zależności od doświadczenia.
# 
# W razie zainteresowania ofertą prosze przesłać CV na adres: ... lub o bezpośredni kontakt pod nr telefonu 12345678. Będę również wdzięczna za wszelkie polecenia.
# 
# Pozdrawiam
# 
# Headhunter
# Recruitment Consultant at CompanyName"""
# Prompt8
# message =f"""Cześć Kostyantyn,
# 
# Czy to dobry moment na zamiany zawodowe? :)
# 
# CompanyName jako partner nr. 1 Mulesoft CompanyName Paractice Development, poszukuje ludzi na projekty dla lokalnych i międzynarodowych klientów.
# Zatrudnienie długoterminowe w oparciu o B2B lub UoP z benefitami i gwarancją ciągłości.
# Bezpłatny dostęp do szkoleń i certyfikacji Mulesoft. Ścieżka kariery niezależnie od formy zatrudnienia.
# Praca zdalna.
# Chętnie opowiem więcej jeśli byłbyś zainteresowany! :)
# 
# Headhunter
# Recruiter/ HR Coordinator"""
# Prompt9
# message =f"""Hello,
# 
# This is Headhunter, a Recruiter working for CompanyName- an American leader in e-commerce market.
# I hope I'm not intruding with my message.
# 
# In a few words- while reviewing your profile for experience and skills, I decided to contact you regarding Remote Software Engineer job opportunities in Integration Development Team.
# 
# We are looking for Mid and Senior talents.
# 
# Please let me know if you would be interested in taking part in the recruitment process or if you have any questions about the role.
# 
# I've provided a link to the job descriptions where you can take a look at the full offer and apply.
# 
# CompanyName:
# https:
# 
# CompanyName:
# 
# https:/
# 
# 
# We offer UoP with salary up to 28 000 Gross/month.
# Fully remote or hybrid work model
# Life Insurance
# Private medical care
# MyBenefit platform (Multisport included)
# Onsite free parking space for employees
# Company performance related bonus
# Referral program with financial bonus and many more.
# 
# Regards,"""
# Prompt10
# message =f"""Hi Kostyantyn
# 
# How are you?
# 
# I have kindly been referred to speak with you as i am currently recruiting for a long term project in Ireland for a Pharmaceutical giant in Ireland, Limerick.
# 
# Your technical experience is very much aligned with the client requirements, as they look to build their Automation team.
# 
# Are you free for a call to discuss the role in more detail? What is the best time and number to call you on?
# 
# Many thanks,
# 
# Headhunter
# Always keen to speak with Construction/Project Managers, CQV professionals, Clean & Black utility personals, Automation engineers, HVAC rockstars!"""
# Prompt11
# message =f"""Can we connect for career discussion!!
# Hi Kostyantyn,
# Greetings!!
# 
# I'm reaching out on behalf of CompanyName Technologies which is a leading provider of IT services and solutions, and we are currently looking for resources to join with one of our clients based out in Poland.
# 
# If fine and interested, kindly help me with your CV and best time to connect for short phone or Teams call.
# 
# Role : MuleSoft Developer
# Location : Remote work within Poland
# Role Type : b2b Contract
# Client: Coforge
# 
# • Knowledge of technologies such as Java (e.g. Springboot framework, Maven), JavaScript (Node.js, JSON), SQL, NoSQL (e.g. MongoDB), SQL, OData
# • Experience working with cloud development (e.g., Azure, AWS, GCP)
# • Experience integrating some enterprise software systems such as SAP ERP, Sharepoint, Marketo, ServiceNow, Salesforce, DocuSign
# • Some knowledge of OAuth 2.0, OpenID Connect, JSON Web Tokens (JWT), SSL, and/or SAML
# • Experience with Jira / Confluence
# • Knowledge of Agile methodologies such as Scrum and Kanban
# • Experience with CI/CD DevOps tools like Git, Azure DevOps etc.
# • Knowledge of monitoring tools like Splunk, Uptrends, Azure Monitors, AWS Cloud Watch, PRTG etc.
# • Experience in enabling monitoring for applications and remediating the issues based on the metrics and threshold alerts.
# 
# Warm regards
# Headhunter"""
# Prompt12
# message =f"""MuleSoft Developer -- Tier 1 Consultancy -- Freelance -- Poland
# Hi Kostyantyn,
# 
# I hope you're having a lovely week.
# 
# I have a MuleSoft Developer opportunity with a Tier 1 recognised Consultancy based in Poland that I wanted to speak to you about.
# 
# This is a freelance/contract opportunity.
# 
# Please respond with a number so I can give you a quick call to discuss in more detail :)
# 
# I look forward to hearing from you.
# 
# Warm Regards,
# Headhunter
# 
# Headhunter
# Key Account Manager at CompanyName"""
# Prompt13
# message =f"""Cześć Kostyantyn!
# 
# Super, że udało nam się nawiązać kontakt!
# 
# Piszę z CompanyName, z propozycją współpracy. Może to najwyższy czas na kolejny krok w życiu zawodowym?
# 
# 📢Rola: 𝗜𝗻𝘁𝗲𝗴𝗿𝗮𝘁𝗶𝗼𝗻 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿
# 💡Zespół: EIC - odpowiedzialny za rozwój i utrzymanie Enterprise Service Bus - opartej na oprogramowaniu TIBCO BusinessWorks
# 🛠 stack: Java / TIBCO BusinessWorks 5/6/CE, services on premise / microservices in cloud / relational DBs / Messaging (JMS/EMS/Kafka)
# 🏠 praca hybrydowa
# UoP, dodatkowo bonus roczny ~10% rocznego wynagrodzenia i podwyższone koszty uzyskania przychodu (60%)
# 
# Czego możesz się spodziewać:
# 🔸 obsługi ponad 160 pojedynczych usług wdrożonych na środowisku produkcyjnym
# 🔸 pracy nad nowymi projektami oraz wsparcia i utrzymania rozwiniętych usług
# 🔸 obecnie skupienia się na integracji z Allegro.cz oraz pracach w obszarze Retail i BackOffice
# 
# Szczegóły: https:/
# 
# Brzmi nieźle? Czekam na wiadomość zwrotną.
# Na początek opowiem ci więcej o procesie rekrutacyjnym i ofercie podczas krótkiej (max 20 min) rozmowy telefonicznej, później ruszymy dalej😊
# 
# Udanego dnia,
# 
# Headhunter
# Talent Sourcer"""
# Prompt14
# message =f"""Exciting Opportunity with CompanyName - Let's Connect!
# Hi Kostyantyn,
# 
# I hope this message finds you well.
# 
# Collabera Digital is hiring a Mulesoft Developer for CompanyName in Poland.
# 
# CompanyName is a global Platinum Salesforce Partner with global delivery teams across EMEA and APAC. CompanyName is a leading Salesforce consulting partner supporting over 1000 Projects and 425 Clients.
# 
# Job Details:
# 1. Develop new Mulesoft functionality to the required specifications.
# 2. Follow Mulesoft development best practices & coding standards.
# 3. Prepare and execute development test cases for applications developed, ensuring full scenario coverage and 100% code coverage in MUnit
# 4. Troubleshoot, debug and fix defects.
# 5. Participate in design & code reviews.
# 6. Meet Sprint development timeline as planned in Sprint planning meetings with quality delivery.
# 
# Please help us with best available time and contact details for a quick discussion.
# 
# Thanks & Best Regards,
# 
# Headhunter
# Senior Talent Specialist - Digital @ Collabera Digital | Expertise in IT Recruitment and Digital Transformation"""
# Prompt15
# message =f"""Hi,
# 
# Hope you are doing good
# 
# Exciting Opportunity :: EAI / MuleSoft Developer :: Remote :: Permanent
# 
# If you are interested please Kindly share your cv to ....
# 
# Best Regards,
# Headhunter"""
# Prompt16
# message =f"""Hello,
# I would like to invite you to join my LinkedIn network. Our professional paths can complement each other.
# Best regards,
#Headhunter"""
# Prompt17
# message =f"""Immediate Requirement:
# 
# Greeting from Bull IT Services!
# 
# Role: Mulesoft Developer
# Location: Poland
# Duration: Permanent (Remote)
# 
# Please Share your CV to Headhunter"""
# Prompt18
# message =f"""Headhunter
# 
# Hello, cheers!
# 
# Greetings from Bull IT services!
# Role : Mulesoft developer
# Location : Poland (Remote)
# Mode : Permanent Employment
# 
# If you are interested,
# Please share your CV to n..."""
# Prompt19
# message =f"""Привіт, Костянтин!
# Міжнародна IT компанія із розробки власного продукту шукає Integration manager.
# Пропонує гнучкий формат роботи і професійний ріст у команді експертів.
# Розповісти більше?)"""
# Prompt20
# message =f"""Hi Kostyantyn,
# Szukam aktualnie dla klienta ze Skandynawii developera Mulesoft, ze znajomością MuleSoft APIs, Anypoint Platform, (REST, JMS, SOAP).
# Full time, long term & forever remote.
# Stawka do EUR 50/h, w zal. od seniority."""
# Prompt21
# message =f"""Hi Kostyantyn,
# 
# I reach out to you with a proposal for a new job as a Senior Mulesoft Developer in Michael Page.
# 
# 💸 23-28k
# 📑 UoP
# 🏡 Remote
# 
# 
# 
# Is it ok? Apply
# 
# Are you looking for something else? Let me know!"""
# Prompt22
# message =f"""
# Hi,
# 
# Hope you are doing great,
# We have a project opportunity on the role of MuleSoft Developer Based in Poland.
# 
# 
# if you are interested please revert back with your updated CV to 
# 
# Thanks and Regards,
# Headhunter"""
# Prompt23
# message =f"""Headhunter 
# 
# 
# Cześć Kostyantyn! Poszukuje Integration Specialist!
# Klient: holenderskie przedsiębiorstwo piwowarskie
# UoP lub B2B (+płatne urlopy). Stawka do uzgodnienia.
# W: MuleSoft/Dell Boomi, Azure API Management
# Remote (2-3x w miesiącu z biura w Krk)
# Porozmawiamy?
# """
# Prompt24
# message =f"""Hi Kostyantyn,
# 
# Hope you are doing good.
# 
# I am a Lead Recruiter from CompanyName.
# 
# We are looking for a "MuleSoft Developer" for a contract in Poland(Remote).
# 
# Kindly advise your interest on the role and if interested do share your CV at ...
# 
# B.R,
# Headhunter."""

# Prompt25
message =f"""Hi,
Job opening for Mulesoft Developer,Contract(Polish),Poland(Remote)
If you are interested, please feel free to reach out on ...

Regards,
Headhunter"""

prompt = f"""
# Your task is to write reply to a linkedin headhunter message.
# \
# Unfortinatelly right now I am not looking for new job.
# \
# I'd like to learn more about the requirements and opportunity
#
# Add something like "hope to stay in contact for future projects"
# 
# Language of a reply should be in the same as message (from male perspective)
# \
# My name is Kostyantyn\
# \
# Additional info: 
#
# Headhunter message: ```{message}```
# """
response = get_completion(prompt)
print(response)

# Start with apology for not replying for a long time, because I was offline in linkedin.\