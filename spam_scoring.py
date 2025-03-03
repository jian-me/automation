def main(input: str) -> int:
    """
    Evaluate the likelihood of a message being spam based on its content.
    
    Args:
        input (str): The message text to analyze for spam indicators
    
    Returns:
        int: Spam likelihood rating from 1-10 (10 being most likely spam)
    """
    # Convert to lowercase for case-insensitive matching
    message = input.lower()

    # Check for specific words that would reduce spam score to 1
    if any(word in message for word in [
        # allow list goes here
        ]):
        return 1
    
    # Define spam indicators and their weights
    spam_indicators = [
        ("urgent" in message, 3),
        ("limited time" in message, 2),
        ("act now" in message, 3),
        ("free offer" in message, 2),
        ("congratulations" in message, 1),
        ("winner" in message, 2),
        ("click here" in message, 2),
        ("exclusive deal" in message, 2),
        ("you've been selected" in message, 3),
        ("churn" in message, 1),  # Potential sales/marketing language
        ("access" in message, 2),
        ("access now" in message, 3),
        ("act" in message, 1),
        ("act immediately" in message, 3),
        ("act now" in message, 3),
        ("action" in message, 1),
        ("action required" in message, 3),
        ("apply here" in message, 2),
        ("apply now" in message, 3),
        ("apply online" in message, 2),
        ("become a member" in message, 2),
        ("before it’s too late" in message, 3),
        ("being a member" in message, 1),
        ("buy" in message, 2),
        ("buy direct" in message, 4),
        ("buy now" in message, 5),
        ("buy today" in message, 5),
        ("call free" in message, 2),
        ("call me" in message, 2),
        ("call now" in message, 3),
        ("can we have a minute of your time?" in message, 5),
        ("cancel now" in message, 3),
        ("cancellation required" in message, 3),
        ("claim now" in message, 2),
        ("click below" in message, 4),
        ("click here" in message, 2),
        ("click me to download" in message, 3),
        ("click now" in message, 3),
        ("click this link" in message, 3),
        ("click to get" in message, 3),
        ("click to remove" in message, 3),
        ("contact us immediately" in message, 4),
        ("deal ending soon" in message, 7),
        ("do it now" in message, 4),
        ("do it today" in message, 4),
        ("don’t delete" in message, 2),
        ("don’t hesitate" in message, 2),
        ("don’t waste time" in message, 3),
        ("exclusive deal" in message, 5),
        ("expire" in message, 2),
        ("expires today" in message, 3),
        ("final call" in message, 5),
        ("for instant access" in message, 4),
        ("for only" in message, 3),
        ("get it away" in message, 4),
        ("get it now" in message, 6),
        ("get now" in message, 5),
        ("get paid" in message, 2),
        ("get started" in message, 2),
        ("get started now" in message, 4),
        ("great offer" in message, 4),
        ("hurry up" in message, 5),
        ("info you requested" in message, 3),
        ("information you requested" in message, 3),
        ("instant" in message, 4),
        ("limited time" in message, 5),
        ("new customers only" in message, 7),
        ("now only" in message, 5),
        ("offer expires" in message, 7),
        ("once in a lifetime" in message, 8),
        ("order now" in message, 5),
        ("order today" in message, 5),
        ("please read" in message, 2),
        ("purchase now" in message, 5),
        ("sign up free" in message, 2),
        ("sign up free today" in message, 4),
        ("supplies are limited" in message, 6),
        ("take action" in message, 4),
        ("take action now" in message, 6),
        ("this won’t last" in message, 6),
        ("time limited" in message, 5),
        ("top urgent" in message, 7),
        ("trial" in message, 4),
        ("urgent" in message, 7),
        ("what are you waiting for?" in message, 5),
        ("while supplies last" in message, 6),
        ("you are a winner" in message, 6),
        ("0 down" in message, 2),
        ("4U" in message, 4),
        ("all natural" in message, 3),
        ("all new" in message, 3),
        ("all-natural" in message, 3),
        ("all-new" in message, 3),
        ("allowance" in message, 2),
        ("as seen on" in message, 3),
        ("as seen on oprah" in message, 5),
        ("at no cost" in message, 3),
        ("auto email removal" in message, 6),
        ("beneficial offer" in message, 6),
        ("beneficiary" in message, 2),
        ("brand new pager" in message, 4),
        ("bulk email" in message, 8),
        ("buying judgements" in message, 9),
        ("buying judgments" in message, 9),
        ("cable converter" in message, 4),
        ("calling creditors" in message, 6),
        ("can you help us?" in message, 5),
        ("cancel at any time" in message, 2),
        ("cannot be combined" in message, 3),
        ("celebrity" in message, 4),
        ("cell phone cancer scam" in message, 9),
        ("cheap" in message, 4),
        ("cheap meds" in message, 9),
        ("cialis" in message, 10),
        ("claims not to be selling anything" in message, 6),
        ("claims to be in accordance with some spam law" in message, 7),
        ("claims to be legal" in message, 2),
        ("clearance" in message, 3),
        ("collect" in message, 1),
        ("cold caller" in message, 3),
        ("cold callers" in message, 3),
        ("cold call" in message, 3),
        ("collect child support" in message, 7),
        ("compare now" in message, 5),
        ("compare online" in message, 4),
        ("compare rates" in message, 4),
        ("compete for your business" in message, 5),
        ("confidentiality" in message, 3),
        ("congratulations" in message, 1),
        ("consolidate debt and credit" in message, 6),
        ("consolidate your debt" in message, 5),
        ("copy accurately" in message, 2),
        ("copy dvds" in message, 6),
        ("cures baldness" in message, 9),
        ("diagnostic" in message, 4),
        ("diet" in message, 4),
        ("dig up dirt on friends" in message, 9),
        ("direct email" in message, 4),
        ("direct marketing" in message, 4),
        ("eliminate debt" in message, 7),
        ("explode your business" in message, 8),
        ("fast viagra delivery" in message, 9),
        ("financial advice" in message, 4),
        ("financing" in message, 4),
        ("financial independence" in message, 6),
        ("financially independent" in message, 6),
        ("for new customers only" in message, 4),
        ("foreclosure" in message, 7),
        ("free" in message, 7),
        ("free access" in message, 6),
        ("free bonus" in message, 6),
        ("free cell phone" in message, 7),
        ("free gift" in message, 7),
        ("free grant money" in message, 8),
        ("free information" in message, 6),
        ("free installation" in message, 6),
        ("free instant" in message, 6),
        ("free iphone" in message, 7),
        ("free laptop" in message, 7),
        ("free leads" in message, 6),
        ("free macbook" in message, 7),
        ("free offer" in message, 6),
        ("free priority mail" in message, 6),
        ("free sample" in message, 6),
        ("free website" in message, 6),
        ("free!" in message, 7),
        ("gift card" in message, 5),
        ("gift certificate" in message, 5),
        ("gift included" in message, 5),
        ("give it away" in message, 6),
        ("giving away" in message, 6),
        ("giving it away" in message, 6),
        ("gold" in message, 4),
        ("great deal" in message, 3),
        ("greetings of the day" in message, 3),
        ("growth hormone" in message, 8),
        ("guarantee" in message, 5),
        ("guaranteed deposit" in message, 6),
        ("guaranteed income" in message, 6),
        ("guaranteed payment" in message, 6),
        ("have you been turned down?" in message, 6),
        ("hello (with no name included)" in message, 3),
        ("hidden charges" in message, 6),
        ("hidden costs" in message, 6),
        ("hidden fees" in message, 6),
        ("high score" in message, 3),
        ("home based business" in message, 6),
        ("home mortgage" in message, 5),
        ("human" in message, 1),
        ("human growth hormone" in message, 8),
        ("if only it were that easy" in message, 5),
        ("important information" in message, 4),
        ("important notification" in message, 4),
        ("instant weight loss" in message, 8),
        ("insurance lose weight" in message, 7),
        ("internet marketing" in message, 5),
        ("investment decision" in message, 4),
        ("it’s effective" in message, 4),
        ("job alert" in message, 4),
        ("junk" in message, 5),
        ("lambo" in message, 9),
        ("laser printer" in message, 5),
        ("last day" in message, 4),
        ("legal notice" in message, 4),
        ("life insurance" in message, 5),
        ("lifetime access" in message, 5),
        ("lifetime deal" in message, 5),
        ("limited amount" in message, 5),
        ("limited number" in message, 5),
        ("limited offer" in message, 5),
        ("limited supply" in message, 4),
        ("limited time offer" in message, 4),
        ("limited time only" in message, 3),
        ("loan" in message, 3),
        ("long distance phone number" in message, 2),
        ("long distance phone offer" in message, 3),
        ("lose weight" in message, 6),
        ("lose weight fast" in message, 8),
        ("lose weight spam" in message, 10),
        ("lottery" in message, 7),
        ("lower interest rate" in message, 4),
        ("lower interest rates" in message, 4),
        ("lower monthly payment" in message, 4),
        ("lower your mortgage rate" in message, 6),
        ("lowest insurance rates" in message, 6),
        ("lowest interest rate" in message, 6),
        ("lowest rate" in message, 3),
        ("lowest rates" in message, 3),
        ("luxury" in message, 2),
        ("luxury car" in message, 2),
        ("mail in order form" in message, 2),
        ("mark this as not junk" in message, 3),
        ("mass email" in message, 7),
        ("medical" in message, 3),
        ("medicine" in message, 3),
        ("meet girls" in message, 8),
        ("meet me" in message, 6),
        ("meet singles" in message, 8),
        ("meet women" in message, 8),
        ("member" in message, 2),
        ("member stuff" in message, 2),
        ("message contains disclaimer" in message, 1),
        ("message from" in message, 1),
        ("millionaire" in message, 5),
        ("millions" in message, 3),
        ("mlm" in message, 7),
        ("multi-level marketing" in message, 8),
        ("near you" in message, 4),
        ("never before" in message, 2),
        ("new domain extensions" in message, 4),
        ("nigerian" in message, 9),
        ("no age restrictions" in message, 4),
        ("no catch" in message, 2),
        ("no claim forms" in message, 2),
        ("no cost" in message, 2),
        ("no credit check" in message, 3),
        ("no credit experience" in message, 3),
        ("no deposit required" in message, 3),
        ("no disappointment" in message, 2),
        ("no experience" in message, 3),
        ("no fees" in message, 2),
        ("no gimmick" in message, 2),
        ("no hidden" in message, 2),
        ("no hidden fees" in message, 2),
        ("no hidden costs" in message, 2),
        ("no interest" in message, 2),
        ("no interests" in message, 2),
        ("no inventory" in message, 2),
        ("no investment" in message, 4),
        ("no investment required" in message, 3),
        ("no medical exams" in message, 3),
        ("no middleman" in message, 2),
        ("no obligation" in message, 2),
        ("no payment required" in message, 2),
        ("no purchase necessary" in message, 2),
        ("no questions asked" in message, 2),
        ("no selling" in message, 2),
        ("no strings attached" in message, 2),
        ("no-obligation" in message, 2),
        ("nominated bank account" in message, 3),
        ("not intended" in message, 1),
        ("not junk" in message, 1),
        ("not scam" in message, 1),
        ("not spam" in message, 1),
        ("notspam" in message, 1),
        ("number 1" in message, 2),
        ("obligation" in message, 2),
        ("off everything" in message, 2),
        ("off shore" in message, 3),
        ("offer extended" in message, 2),
        ("offers" in message, 2),
        ("offshore" in message, 3),
        ("one hundred percent" in message, 2),
        ("one-time" in message, 2),
        ("online biz opportunity" in message, 6),
        ("online degree" in message, 5),
        ("online income" in message, 6),
        ("online job" in message, 5),
        ("order shipped by" in message, 2),
        ("order status" in message, 2),
        ("orders shipped by" in message, 2),
        ("orders shipped by shopper" in message, 8),
        ("outstanding value" in message, 2),
        ("outstanding values" in message, 2),
        ("password" in message, 5),
        ("passwords" in message, 7),
        ("pay your bills" in message, 2),
        ("per year" in message, 3),
        ("per month" in message, 2),
        ("perfect" in message, 2),
        ("please open" in message, 4),
        ("presently" in message, 2),
        ("print form signature" in message, 4),
        ("print from signature" in message, 4),
        ("print out and fax" in message, 4),
        ("priority mail" in message, 4),
        ("privately owned funds" in message, 3),
        ("prizes" in message, 6),
        ("problem with shipping" in message, 5),
        ("problem with your order" in message, 5),
        ("produced and sent out" in message, 3),
        ("profit" in message, 2),
        ("promise you" in message, 7),
        ("purchase" in message, 2),
        ("pure profits" in message, 5),
        ("real thing" in message, 3),
        ("rebate" in message, 6),
        ("reduce debt" in message, 7),
        ("refinance home" in message, 7),
        ("refinanced home" in message, 7),
        ("refund" in message, 6),
        ("regarding" in message, 2),
        ("removal instructions" in message, 6),
        ("removes wrinkles" in message, 8),
        ("replica watches" in message, 10),
        ("request now" in message, 3),
        ("request today" in message, 3),
        ("requires initial investment" in message, 8),
        ("requires investment" in message, 8),
        ("reverses aging" in message, 10),
        ("risk free" in message, 5),
        ("rolex" in message, 10),
        ("round the world" in message, 2),
        ("safeguard notice" in message, 4),
        ("sale" in message, 2),
        ("sales" in message, 2),
        ("save big" in message, 3),
        ("save big month" in message, 3),
        ("save money" in message, 2),
        ("save now" in message, 2),
        ("score with babes" in message, 10),
        ("search engine optimisation" in message, 4),
        ("section 301" in message, 4),
        ("see for yourself" in message, 3),
        ("seen on" in message, 3),
        ("serious" in message, 2),
        ("serious case" in message, 5),
        ("serious offer" in message, 5),
        ("serious only" in message, 5),
        ("sex" in message, 10),
        ("shop now" in message, 2),
        ("shopper" in message, 4),
        ("shopping spree" in message, 3),
        ("snoring" in message, 5),
        ("social security number" in message, 8),
        ("spam" in message, 10),
        ("spam free" in message, 2),
        ("special deal" in message, 4),
        ("special discount" in message, 4),
        ("special for you" in message, 4),
        ("special offer" in message, 4),
        ("stainless steel" in message, 5),
        ("stock alert" in message, 6),
        ("stock disclaimer statement" in message, 6),
        ("stock pick" in message, 6),
        ("stocks/stock pick/stock alert" in message, 6),
        ("stop calling me" in message, 6),
        ("stop emailing me" in message, 6),
        ("stop further distribution" in message, 7),
        ("stop snoring" in message, 8),
        ("strong buy" in message, 6),
        ("stuff on sale" in message, 2),
        ("subject to" in message, 2),
        ("subject to cash" in message, 7),
        ("subscribe" in message, 2),
        ("subscribe for free" in message, 3),
        ("subscribe now" in message, 3),
        ("super promo" in message, 4),
        ("supplies" in message, 2),
        ("this is an ad" in message, 5),
        ("the best rates" in message, 3),
        ("the following form" in message, 4),
        ("they make a claim or claims that they’re in accordance with spam law" in message, 7),
        ("they try to keep your money no refund" in message, 9),
        ("they’re just giving it away" in message, 7),
        ("this isn’t junk" in message, 2),
        ("this isn’t spam" in message, 2),
        ("this isn’t a scam" in message, 2),
        ("timeshare" in message, 6),
        ("timeshare offers" in message, 7),
        ("traffic" in message, 3),
        ("trial unlimited" in message, 3),
        ("u.s. dollars" in message, 2),
        ("undisclosed" in message, 6),
        ("undisclosed recipient" in message, 6),
        ("university diplomas" in message, 8),
        ("unsecured credit" in message, 6),
        ("unsecured debt" in message, 6),
        ("unsolicited" in message, 9),
        ("unsubscribe" in message, 5),
        ("urgent response" in message, 7),
        ("euros" in message, 2),
        ("vacation" in message, 6),
        ("vacation offers" in message, 7),
        ("valium" in message, 10),
        ("viagra" in message, 10),
        ("vicodin" in message, 10),
        ("vip" in message, 6),
        ("visit our website" in message, 4),
        ("wants credit card" in message, 8),
        ("warranty expired" in message, 6),
        ("we hate spam" in message, 2),
        ("we honor all" in message, 3),
        ("website visitors" in message, 4),
        ("weekend getaway" in message, 5),
        ("weight loss" in message, 7),
        ("what’s keeping you?" in message, 5),
        ("while available" in message, 4),
        ("while in stock" in message, 4),
        ("while stocks last" in message, 5),
        ("while you sleep" in message, 6),
        ("who really wins?" in message, 6),
        ("win" in message, 3),
        ("winner" in message, 7),
        ("winning" in message, 4),
        ("won" in message, 5),
        ("xanax" in message, 10),
        ("xxx" in message, 10),
        ("you have been chosen" in message, 7),
        ("you have been selected" in message, 7),
        ("your chance" in message, 7),
        ("your status" in message, 4),
        ("zero chance" in message, 4),
        ("zero percent" in message, 4),
        ("zero risk" in message, 4),
        ("#1" in message, 3),
        ("% free" in message, 4),
        ("% satisfied" in message, 3),
        ("0% risk" in message, 4),
        ("100% free" in message, 6),
        ("100% more" in message, 5),
        ("100% off" in message, 5),
        ("100% satisfied" in message, 5),
        ("0.999" in message, 3),
        ("0.99" in message, 3),
        ("access for free" in message, 4),
        ("additional income" in message, 5),
        ("amazing offer" in message, 8),
        ("amazing stuff" in message, 7),
        ("be amazed" in message, 6),
        ("be surprised" in message, 4),
        ("be your own boss" in message, 7),
        ("believe me" in message, 6),
        ("best bargain" in message, 7),
        ("best deal" in message, 6),
        ("best offer" in message, 6),
        ("best price" in message, 6),
        ("best rates" in message, 6),
        ("big bucks" in message, 7),
        ("bonus" in message, 5),
        ("boss" in message, 5),
        ("can’t live without" in message, 6),
        ("consolidate debt" in message, 6),
        ("double your cash" in message, 6),
        ("double your income" in message, 6),
        ("drastically reduced" in message, 5),
        ("earn extra cash" in message, 6),
        ("earn money" in message, 5),
        ("eliminate bad credit" in message, 6),
        ("expect to earn" in message, 4),
        ("extra" in message, 2),
        ("extra cash" in message, 3),
        ("extra income" in message, 3),
        ("fantastic" in message, 3),
        ("fantastic deal" in message, 4),
        ("fantastic offer" in message, 4),
        ("fast" in message, 5),
        ("fast cash" in message, 6),
        ("financial freedom" in message, 5),
        ("free consultation" in message, 3),
        ("free hosting" in message, 3),
        ("free info" in message, 4),
        ("free investment" in message, 6),
        ("free membership" in message, 6),
        ("free money" in message, 10),
        ("free preview" in message, 4),
        ("free quote" in message, 7),
        ("free trial" in message, 5),
        ("full refund" in message, 2),
        ("get out of debt" in message, 6),
        ("giveaway" in message, 3),
        ("guaranteed" in message, 7),
        ("increase sales" in message, 3),
        ("increase traffic" in message, 3),
        ("incredible deal" in message, 5),
        ("join billions" in message, 3),
        ("join millions" in message, 3),
        ("join millions of americans" in message, 3),
        ("join thousands" in message, 3),
        ("lower rates" in message, 3),
        ("lowest price" in message, 3),
        ("make money" in message, 5),
        ("million" in message, 5),
        ("million dollars" in message, 6),
        ("miracle" in message, 7),
        ("money back" in message, 4),
        ("month trial offer" in message, 4),
        ("more internet traffic" in message, 4),
        ("number one" in message, 4),
        ("one hundred percent guaranteed" in message, 6),
        ("one time" in message, 3),
        ("pennies a day" in message, 3),
        ("potential earnings" in message, 4),
        ("prize" in message, 5),
        ("promise" in message, 5),
        ("pure profit" in message, 4),
        ("risk-free" in message, 6),
        ("satisfaction guaranteed" in message, 4),
        ("save big money" in message, 4),
        ("save up to" in message, 3),
        ("special promotion" in message, 4),
        ("the best" in message, 3),
        ("thousands" in message, 3),
        ("unbeatable offer" in message, 5),
        ("unbelievable" in message, 6),
        ("unlimited" in message, 3),
        ("unlimited trial" in message, 4),
        ("wonderful" in message, 3),
        ("you will not believe your eyes" in message, 5),
        ("$$$" in message, 6),
        ("50% off" in message, 5),
        ("a few bob" in message, 2),
        ("accept cash cards" in message, 3),
        ("accept credit cards" in message, 3),
        ("affordable" in message, 2),
        ("affordable deal" in message, 2),
        ("avoid bankruptcy" in message, 4),
        ("bad credit" in message, 5),
        ("bankruptcy" in message, 6),
        ("bargain" in message, 4),
        ("billing address" in message, 2),
        ("billion" in message, 6),
        ("billion dollars" in message, 7),
        ("billionaire" in message, 4),
        ("card accepted" in message, 2),
        ("cards accepted" in message, 2),
        ("cash" in message, 3),
        ("cash bonus" in message, 3),
        ("cash out" in message, 3),
        ("cash-out" in message, 3),
        ("cashcashcash" in message, 6),
        ("casino" in message, 5),
        ("cents on the dollar" in message, 4),
        ("check" in message, 2),
        ("check or money order" in message, 4),
        ("claim your discount" in message, 3),
        ("costs" in message, 2),
        ("credit" in message, 4),
        ("credit bureaus" in message, 5),
        ("credit card" in message, 5),
        ("credit card offers" in message, 5),
        ("credit or debit" in message, 4),
        ("deal" in message, 2),
        ("debt" in message, 5),
        ("discount" in message, 3),
        ("dollars" in message, 3),
        ("double your" in message, 4),
        ("double your wealth" in message, 4),
        ("digital health" in message, 4),
        ("earn" in message, 4),
        ("earn $" in message, 4),
        ("earn cash" in message, 4),
        ("earn extra income" in message, 4),
        ("earn from home" in message, 4),
        ("earn monthly" in message, 4),
        ("earn per month" in message, 4),
        ("earn per week" in message, 4),
        ("earn your degree" in message, 4),
        ("easy income" in message, 3),
        ("easy terms" in message, 3),
        ("f r e e" in message, 8),
        ("for free" in message, 3),
        ("for just $" in message, 3),
        ("for just $ (amount)" in message, 3),
        ("for just $xxx" in message, 3),
        ("get money" in message, 4),
        ("get your money" in message, 4),
        ("hidden assets" in message, 6),
        ("huge discount" in message, 4),
        ("income" in message, 4),
        ("income from home" in message, 4),
        ("increase revenue" in message, 4),
        ("increase sales/traffic" in message, 4),
        ("increase your chances" in message, 4),
        ("initial investment" in message, 4),
        ("instant earnings" in message, 4),
        ("instant income" in message, 4),
        ("insurance" in message, 4),
        ("investment" in message, 4),
        ("investment advice" in message, 4),
        ("investors" in message, 4),
        ("lifetime" in message, 3),
        ("loans" in message, 6),
        ("make $" in message, 6),
        ("marketing associate" in message, 3),
        ("money" in message, 3),
        ("money making" in message, 4),
        ("money-back guarantee" in message, 4),
        ("money-making" in message, 4),
        ("monthly payment" in message, 2),
        ("mortgage" in message, 5),
        ("mortgage rates" in message, 5),
        ("not interested" in message, 2),
        ("one hundred percent free" in message, 3),
        ("only $" in message, 6),
        ("price" in message, 2),
        ("price protection" in message, 3),
        ("prices" in message, 2),
        ("profits" in message, 4),
        ("quote" in message, 2),
        ("rates" in message, 2),
        ("refinance" in message, 5),
        ("save $" in message, 5),
        ("serious cash" in message, 4),
        ("subject to credit" in message, 4),
        ("us dollars" in message, 2),
        ("why pay more?" in message, 3),
        ("your income" in message, 4),
        ("acceptance" in message, 2),
        ("accordingly" in message, 1),
        ("account-based marketing" in message, 3),
        ("accounts" in message, 2),
        ("addresses" in message, 2),
        ("addresses on cd" in message, 5),
        ("beverage" in message, 1),
        ("confidentiality on all orders" in message, 2),
        ("confidentially on all orders" in message, 2),
        ("content marketing" in message, 3),
        ("digital marketing" in message, 3),
        ("dormant" in message, 2),
        ("email extractor" in message, 8),
        ("email harvest" in message, 8),
        ("email marketing" in message, 7),
        ("extract email" in message, 8),
        ("freedom" in message, 2),
        ("friend" in message, 2),
        ("hidden" in message, 3),
        ("home based" in message, 2),
        ("home employment" in message, 2),
        ("home-based" in message, 2),
        ("home-based business" in message, 2),
        ("homebased business" in message, 2),
        ("if you no longer wish to receive" in message, 8),
        ("important information regarding" in message, 6),
        ("in accordance with laws" in message, 3),
        ("increase your sales" in message, 5),
        ("internet market" in message, 3),
        ("maintained" in message, 2),
        ("marketing" in message, 3),
        ("marketing solution" in message, 3),
        ("marketing solutions" in message, 3),
        ("medium" in message, 2),
        ("message contains" in message, 6),
        ("multi level marketing" in message, 8),
        ("never" in message, 2),
        ("one time mailing" in message, 7),
        ("online marketing" in message, 3),
        ("online pharmacy" in message, 9),
        ("opt in" in message, 5),
        ("pre-approved" in message, 5),
        ("problem" in message, 2),
        ("removal" in message, 4),
        ("reserves the right" in message, 3),
        ("reverses" in message, 2),
        ("satisfaction" in message, 2),
        ("search engine" in message, 5),
        ("search engine listings" in message, 6),
        ("search engines" in message, 5),
        ("sent in compliance" in message, 3),
        ("startups" in message, 5),
        ("success" in message, 2),
        ("teen" in message, 5),
        ("terms and conditions" in message, 3),
        ("warranty" in message, 5),
        ("web traffic" in message, 3),
        ("wife" in message, 3),
        ("work at home" in message, 3),
        ("work from home" in message, 3),
        ("corporate" in message, 5),
        ("sports" in message, 5),
        ("calendly" in message, 5),
        ("developers" in message, 3),
        ("india" in message, 3),
        ("don't miss anything" in message, 3),
        ("facebook" in message, 4),
        ("linked" in message, 4),
        ("instagram" in message, 5),
        ("acquire" in message, 2)
    ]
    
    # Calculate spam score
    spam_score = sum(weight for indicator, weight in spam_indicators if indicator)
    
    # Normalize score to 1-10 range
    spam_rating = min(max(spam_score, 1), 10)
    
    return spam_rating