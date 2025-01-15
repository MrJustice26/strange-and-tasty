import re
data = """
198,Fresh Strawberry Pie,"[""1 qt. strawberries"", ""3/4 c. water"", ""pinch of salt"", ""1 c. sugar"", ""3 Tbsp. cornstarch"", ""dash of cinnamon""]"
221,Mexican Casserole,"[""Fritos or Doritos"", ""1 lb. ground beef"", ""1 onion"", ""1 can rotel"", ""1 can mushroom soup"", ""1 (12 oz.) can pet milk (can use fat free)"", ""Grated cheese""]"
231,Ranch Style Baked Beans Casserole,"[""2 Tbsp. margarine"", ""1 lb. ground beef"", ""1/2 c. water"", ""1 c. catsup"", ""2 Tbsp. prepared mustard"", ""2 tsp. vinegar"", ""2 (1 lb.) cans pork and beans in tomato sauce"", ""1 (1 lb.) can kidney beans, drained""]"
275,Angel Food Cake,"[""1 cup sifted cake flour"", ""1 1/2 cups sugar"", ""1 1/2 cups egg white (about a dozen)"", ""3/4 tsp. salt"", ""1 tsp. vanilla"", ""1/2 tsp. almond flavoring""]"
347,Chicken-Cheese Ball,"[""1 small can chicken (all white meat)"", ""8 oz. cream cheese, softened"", ""1 Tbsp. minced onion"", ""1 Tbsp. mayonnaise"", ""chopped pecans"", ""maraschino cherry for garnish (if desired)""]"
443,Fruit Cocktail Cake,"[""1 (No. 303) can fruit cocktail (juice also)"", ""1 tsp. vanilla"", ""2 tsp. soda"", ""1 tsp. cinnamon"", ""2 c. flour"", ""1/2 c. brown sugar"", ""1 c. pecans, chopped""]"
497,Creamy Cheese Crab Dip,"[""1 (8 oz.) and 1 (3 oz.) pkg. Philadelphia cream cheese"", ""1/2 c. white wine"",""1/8 tsp. garlic powder""]"
565,Pork Medallions,"[""1 lb. lean, boneless pork tenderloins, thinly sliced"", ""3 cloves garlic"", ""1/4 tsp. rosemary"", ""2 1/2 Tbsp. lemon juice (fresh)"", ""1/4 tsp. salt"", ""1/4 tsp. black pepper""]"
630,Chicken & Spaghetti Casserole,"[""1 box spaghetti"", ""1/2 c chopped onion"", ""1/2 c celery"", ""1/2 tsp garlic salt"", ""3 chicken breasts"", ""1/2 c chopped bell pepper"", ""1 can mashed tomatoes"", ""1/4 tsp red pepper""]"
782,Sausage Casserole(Microwave),"[""1 lb. pork sausage"", ""3/4 c. diced onion"", ""3/4 c. diced green pepper"", ""1 Tbsp. sugar"", ""1 Tbsp. chili powder"", ""1 tsp. salt"", ""8 oz. macaroni, cooked"", ""1 c. dairy sour cream""]"
925,Hawaiian Carrots,"[""1 lb. pkg. carrots"", ""1 (No. 2) can and 1 small can crushed pineapple, drained"", ""3 Tbsp. cornstarch"", ""1/2 c. brown sugar""]"
1071,Mini Raisin Nut Breads,"[""4 c. boiling water"", ""4 tsp. baking soda"", ""4 eggs"", ""3 c. sugar"", ""7 c. flour"", ""4 tsp. vanilla"", ""2 tsp. salt"", ""4 c. nuts, coarsely chopped"", ""Crisco (for greasing cans)""]"
1140,Roasted Potatoes,"[""1 envelope onion or mushroom soup mix"", ""1/4 c. butter, melted"", ""1 tsp. thyme leaves"", ""1 tsp. marjoram"", ""1/4 tsp. pepper"", ""2 lb. potatoes, sliced""]"
1211,Golden Cream Potato Soup,"[""3 c. chopped potatoes"", ""1 c. water"", ""1/2 c. carrot slices"", ""1/4 c. chopped onion"", ""1 tsp. parsley flakes"", ""1 chicken bouillon cube"", ""1/2 tsp. salt"", ""dash of pepper"", ""1 1/2 c. milk"", ""2 Tbsp. flour"", ""1/2 lb. Velveeta cheese, cubed"", ""1/2 pkg. frozen broccoli (optional)"", ""cooked crumbled bacon (optional)""]"
1284,Carrot Bars,"[""2 eggs, beaten"", ""1 tsp. soda"", ""1/2 tsp. salt"", ""1 large jar baby strained carrots"",""1 tsp. cinnamon"", ""1 c. flour"", ""1/2 c. oil"", ""1/4 c. nuts""]"
1363,Strawberry Pie,"[""3 Tbsp. strawberry Jell-O"", ""3 Tbsp. cornstarch"", ""1 frozen pie shell"", ""1 c. sugar"", ""Cool Whip""]"
1517,Salsa Sauce,"[""1 qt. tomatoes"", ""1 onion, chopped"", ""1 clove garlic"", ""1 green pepper"", ""1 hot pepper"", ""1/2 c. vinegar"", ""1 tsp. salt"", ""1 tsp. sugar"", ""1/2 tsp. cumin"", ""dash of cayenne pepper"", ""1/2 tsp. oregano""]"
1588,Sour Cream 'N Dill Chicken,"[""8 to 10 chicken pieces, skinned"", ""pepper"", ""1 envelope dry onion soup mix"", ""1 c. (8 oz.) sour cream"", ""1 Tbsp. lemon juice"", ""1 Tbsp. fresh dill, chopped or 1 tsp. dill weed"", ""1 (4 oz.) can sliced mushrooms, drained"", ""paprika"", ""cooked wide egg noodles (optional)""]"
1713,Corn Chowder,"[""1 can corn"", ""3 slices bacon, cooked and browned"", ""1 Tbsp. chopped onion"", ""1 pt. milk"", ""salt and pepper""]"
1792,The Early'S 3-Layer Squash Casserole,"[""12 medium squash"", ""1 small onion"", ""8 oz. sour cream"", ""12 oz. sharp hard cheese, grated"", ""4 oz. melted butter"", ""salt and pepper to taste"", ""other spices of your choice may be added""]"
1890,Better Than Sex Cake,"[""1 box yellow cake mix"", ""4 eggs"", ""1 small box vanilla instant pudding"", ""1/2 c. oil"", ""1/2 c. water"", ""8 oz. sour cream"", ""6 oz. pkg. chocolate chips"", ""1/2 c. chopped pecans""]"
1959,Hummingbird Cake,"[""3 c. flour"", ""1 tsp. soda"", ""1/2 tsp. salt"",""1 tsp. cinnamon"", ""3 eggs, beaten"", ""3/4 c. oil"", ""1 1/2 tsp. vanilla"", ""1 (8 oz.) can crushed pineapple"", ""1 1/2 c. chopped pecans"", ""1 3/4 c. mashed bananas"", ""1/2 c. oleo, softened"", ""1 (8 oz.) cream cheese"", ""1 lb. powdered sugar"", ""1 tsp. vanilla""]"
2060,Hickory Stick,"[""5 lb. ground beef"", ""5 tsp. Morton Tender Quick salt"", ""2 1/2 tsp. regular salt"", ""1/2 tsp. red pepper"", ""2 1/2 tsp. garlic salt"", ""2 tsp. coarse black pepper"", ""2 1/2 tsp. mustard seed""]"
3076,Turmeric Cauliflower Rice,"['500 g cauliflower', '5 g turmeric', '30 ml olive oil']"
2272,Cranberry Jello Salad,"[""1 (6 oz.) pkg. raspberry jello"", ""1 (16 oz.) can cranberry sauce"", ""1/2 c. ginger ale""]"
2364,Popcorn Balls,"[""1 c. sugar"", ""1/3 c. water"", ""1/3 c. light corn syrup"", ""1/4 c. butter"", ""7 c. popped corn"", ""1 tsp. vanilla""]"
2465,Pineapple Chutney,"[""2 limes"", ""1 jalapeno chile finely chopped"", ""3/4 c. brown sugar"", ""2 Tbsp. minced fresh ginger"", ""1/2 tsp. salt"", ""1 c. pineapple tidbits or ripe one chopped small"", ""2 oranges peeled and chopped or can of mandarins"", ""1 c. dark raisins"", ""1 can tomato soup"", ""1-8 oz. cream cheese"", ""1 1/2 envelopes of knox gelatin"", ""2 diced hard boiled eggs"", ""3/4 cup diced celery"", ""1/2 cup diced onion"", ""2 drops Tabasco or horseradish"", ""1 cup mayonnaise"", ""2 cans baby shrimp (10 oz. cans)""]"
2540,Broccoli Corn Casserole,"[""1 (8 oz.) pkg. frozen broccoli"",""1 pkg. Stove Top stuffing"", ""3 Tbsp. butter"", ""3 beaten eggs""]"
3145,Banana Oat Pancakes,"['2 bananas','2 eggs', '10 g cinnamon']"
3143,Vegetable Stir-Fry,"['200 g mixed vegetables', '50 ml soy sauce', '10 ml sesame oil']"
3125,Berry Yogurt Parfait,"['200 g Greek yogurt', '100 g mixed berries']"
3120,Lentil Veggie Burgers,"['200 g lentils', '10 g garlic']"
2141,Monkey Bread,"[""4 cans (10 biscuits in each) buttermilk biscuits"", ""1 1/2 sticks butter or margarine""]"
3101,Avocado Toast,"['2 slices bread', '5 g chili flakes']"
3076,Turmeric Cauliflower Rice,"['500 g cauliflower', '5 g turmeric', '30 ml olive oil']"
3038,Mango Avocado Salsa,"['1 diced mango', '60 ml diced red onion']"
3003,Sushi Tacos,"['240 g sushi rice', '4 sheets of nori']"
2969,Heavenly Rice,"[""2 c. cooked, drained rice"", ""1 medium bowl whipped cream"", ""1 small pkg. small marshmallows"", ""1 small can drained, crushed pineapple"", ""few drops red food coloring""]"
2915,Twinkie Cake,"[""1 box Twinkie cakes"", ""1 large can pineapple"", ""3 bananas"", ""1 jar cherries"", ""1 c. chopped pecans""]"
2882,Benne Cookies,"[""1/4 lb. butter"", ""1 c. sugar"", ""1 egg"", toasted"", ""1/2 tsp. baking soda in 1 tsp. water"", ""1 tsp. vanilla""]"
2846,Chewy Chocolate Chip Cookies,"[""3 1/2 c. flour"", ""1 tsp. baking soda"", ""1 1/2 c. softened margarine"", ""1/4 tsp. salt (optional)"", ""1 tsp. vanilla"", ""2 eggs or 3 egg whites"", ""1 pkg. (12 oz.) semi-sweet real chocolate chips""]"
2989,Red Lentil Soup With Garlic Croutons,"[""1 lb 2 oz red lentils"", ""1/4 c olive oil"", ""1 large onion"", ""1 1/2 tsp salt"", ""1/2 tsp pepper"", ""1 1/2 tsp cumin""]"
3074,Savory Cheese Scones,"['200 g flour', '150 ml milk']"
3146,Grilled Vegetable Skewers,"['200 g zucchini', '30 ml olive oil']"
3132,Spinach Feta Stuffed Chicken,"['4 chicken breasts', '10 ml olive oil']"
3044,Pineapple Curry Pizza,"['1 pizza crust', '120 ml curry sauce']"
2988,Quickie Broccoli Casserole,"[""2 boxes broccoli (16 oz. each), ""1 can cream of mushroom soup (10 1/2 oz.)"", ""1 c. Cheddar cheese, shredded"", ""Ritz style crackers"", ""melted or squeeze margarine""]"
2957,Strawberry-Yogurt Drink,"[ ""8 oz. plain yogurt"", ""1 large banana, cut up"", ""8 ice cubes""]"
2946,French Dip Sandwiches,"[""1 can beef consomm"", ""1 pkg. Au Jus"", ""4 lb. roast, boneless""]"
2929,Pork Chops With Kraut,"[""6 pork chops"", ""pepper"", ""chopped garlic"", ""1 pt. beer""]"
2870,Spicy Bean Dip,"[""1 lb. hamburger"",""1 (8 oz.) can tomato sauce"", ""1/4 c. catsup"", ""3/4 tsp. oregano"", ""1 tsp. sugar"", ""8 oz. cream cheese, softened"", ""1/3 c. Parmesan cheese""]"
2814,Vegetable Casserole,"[""1 can French-style green beans"", ""1 can whole kernel corn"", ""8 oz. sour cream"", ""1 can cream of chicken or mushroom soup"", ""1 tube Ritz crackers, crushed"", ""1 stick butter or margarine, melted""]"
2726,Hobo Stew(Easy),"[""1 lb. ground beef"", ""2 wieners, diced"", ""1 envelope onion gravy mix"",""1 c. water""]"
2663,Creamy Chocolate Pie(Makes 2 Pies),"[ ""6 eggs, separated"", ""4 Tbsp. flour"", ""2 Tbsp. cocoa"", ""1 tsp. vanilla"", ""2 Tbsp. butter or oleo""]"
2608,Zucchini Casserole,"[""1 c. sharp Cheddar cheese, melted to pour on top"", ""1 small onion, chopped"", ""1 large zucchini""]"
2596,Banana Nut Bread,"[""1/2 c. oil"", ""1 c. sugar"", ""2 eggs"", ""1 tsp. vanilla"", ""2 c. flour"", ""3 to 4 bananas (ripe)"", ""1 c. chopped nuts""]"
2532,Scalloped Potatoes,"[""1/3 c. margarine"", ""1/2 c. minced onion"", ""1/3 c. flour"", ""3 c. milk"", ""1/4 tsp. dry mustard"", ""1/8 tsp. pepper (black)"", ""10 c. thinly sliced potatoes"", ""1/4 tsp. paprika""]"
2494,Devil'S Food Cake,"[""1 stick margarine"", ""1 c. water"", ""4 Tbsp. cocoa"", ""1/2 c. Wesson oil"", ""2 c. sugar"", ""2 eggs, slightly beaten"", ""1/2 c. buttermilk"", ""1 tsp. cinnamon"", ""1 tsp. vanilla"", ""1 tsp. soda""]"
2448,Green Bean Casserole,"[""1/2 c. butter"", ""1/4 c. flour"", ""1 1/2 c. milk"", ""1 3 oz. can mushroom"", ""2 tsp. soy sauce"", ""1/3 c. onions"", ""1 tsp. salt"", ""dash of pepper"", ""1 tsp. accent seasonings"", ""2 cans of green beans"", ""1 can of water chestnuts""]"
2418,Peanut Butter Pie,"[""1 (3 oz.) pkg. cream cheese"", ""1 (9 oz.) Cool Whip"", ""1 c. crunchy peanut butter"", ""1 (9-inch) graham cracker crust""]"
2405,Creamy Potato Bake(This Is A Hit At Parties!),"[""2 c. half and half"", ""1/4 c. butter or margarine"", ""1 c. crunchy peanut butter"", ""1/2 tsp. salt"", ""2 (12 oz.) pkg. frozen shredded hash brown potatoes, thawed"", ""1/2 c. freshly grated Parmesan cheese""]"
2263,Lemon Icebox Pie,"[""vanilla wafers"", ""1 can Eagle Brand milk"", ""1 artificial lemon"", ""1 (8 oz.) Cool Whip"", ""1 c. crunchy peanut butter"",]"
2182,Chocolate Chip Cookie,"[""3/4 c. butter flavored Crisco"", ""1 1/4 c. brown sugar"", ""2 Tbsp. milk"", ""1 Tbsp. vanilla"", ""1 egg"", ""1 c. crunchy peanut butter"",""1 3/4 c. all-purpose flour"", ""1 tsp. salt"", ""3/4 tsp. baking soda"", ""1 c. semi-sweet chocolate chips"", ""1 c. chopped pecans""]"
2154,Granny'S Fruit Cake,"[""2 2/3 c. cake flour"", ""2 1/2 tsp. baking powder"", ""1/2 tsp. salt"", ""3/4 c. butter or margarine"", ""1 3/4 c. sugar"", ""1 c. crunchy peanut butter"", ""4 eggs or equivalent egg substitute"", ""1 c. milk or skim milk"", ""2 tsp. vanilla extract"", ""1/3 c. oil"", ""1/2 c. each: peanuts or mixed nuts, walnuts, pecans, almonds, raisins, mixed dried fruit or anything else you like""]"
2104,Egg Custard Pie,"[""4 eggs (whole)"", ""1 c. sugar"", ""2 c. milk, scalded"", ""1 Tbsp. vanilla"", ""1 c. crunchy peanut butter"",]"
2071,Oven Fried Potatoes,"[""red potatoes"", ""1/4 c. Crisco"", ""salt, pepper, garlic salt and onion salt"", ""1/2 to 1 stick margarine"", ""1 c. crunchy peanut butter"",]"
2050,Corn Casserole,"[""1 (16 oz.) can creamed corn"", ""1 stick margarine, melted (1/2 c.)"", ""2 eggs"", ""1 (8 oz.) carton sour cream"", ""1 box Jiffy cornbread mix"", ""1 (16 oz.) can kernel corn, drained""]"
2012,Bacon Nuts,"[""1 can water chestnuts, drained (8 oz.)"", ""1/4 c. soy sauce"", ""1/2 lb. bacon"", ""1 stick margarine, melted (1/2 c.)"",]"
1957,Gumdrop Fruitcake,"[""1 lb. colorful gumdrops, cut in 4 pieces (do not use licorice flavored gumdrops)"", ""1 stick margarine, melted (1/2 c.)"",""1 (10 oz.) pkg. pitted dates, chopped"", ""1 c. raisins"", ""1 c. chopped pecans or walnuts"", ""1 box yellow cake mix"", ""1 (20 oz.) can apple pie filling"", ""1 Tbsp. cinnamon or apple pie spice"", ""3 eggs""]"
1902,Crepes(French),"[""1 1/2 c. all-purpose flour"", ""1/2 tsp. baking powder"", ""1/2 tsp. salt"", ""1 stick margarine, melted (1/2 c.)"", ""1 Tbsp. sugar"", ""2 c. milk"", ""2 eggs"", ""1/2 tsp. vanilla"", ""2 Tbsp. butter""]"
1865,Good Friday"" Vegetable Soup","[""1/4 c. butter"", ""3 medium carrots, sliced"", ""2 medium onions"", ""1 c. shredded cabbage"", ""1 stick margarine, melted (1/2 c.)"", ""1/4 c. chopped parsley"", ""1/2 tsp. salt"", ""2 (13 3/4 oz.) cans chicken broth"", ""1 (9 oz.) pkg. French-cut green beans"", ""1/2 tsp. caraway seed"", ""1 (16 oz.) pkg. American cheese slices""]"
1811,Grandmaw'S Brownies,"[""3/4 c. flour"", ""1 1/4 c. sugar"", ""1 stick margarine, melted (1/2 c.)"", ""1/2 tsp. baking powder"", ""1/2 tsp. salt"", ""1/2 c. cocoa"", ""1 stick margarine, melted (1/2 c.)"", ""1/2 c. powdered milk"", ""2 eggs"", ""1/2 c. shortening"", ""2 eggs"", ""3 Tbsp. tap water"", ""1 tsp. vanilla"", ""1 c. chopped pecans""]"
1778,Microwave Caramels,"[""1 c. butter or margarine"", ""1 stick margarine, melted (1/2 c.)"", ""1 c. sugar"", ""1 c. light brown sugar"", ""1 c. light corn syrup"", ""1 stick margarine, melted (1/2 c.)"", ""1 can sweetened condensed milk"", ""1 tsp. vanilla"", ""1 c. nuts (optional)""]"
1747,Jambalaya,"[""2 c. ham, cut in cubes"", ""1 stick margarine, melted (1/2 c.)"", ""1 Tbsp. butter or margarine"", ""1/2 c. chopped onion"", ""1/2 c. chopped green pepper"", ""1 clove garlic, minced"", ""1 (1 lb.) can stewed tomatoes"", ""1 1/2 c. water"", ""1/2 tsp. salt"", ""1/2 tsp. thyme, crushed"", ""1/4 tsp. hot pepper sauce"", ""1 c. uncooked rice""]"
1716,Teriyaki Chicken Wings,"[""1/2 c. soy sauce"", ""1 stick margarine, melted (1/2 c.)"", ""1/2 c. brown sugar"", ""1 clove garlic"", ""2 tsp. ground ginger"", ""1 tsp. m.s.g."", ""1/2 tsp. pepper"", ""20 chicken wings""]"
1682,Fudgie Brownies,"[""1/2 c. plus 2 tsp. butter"", ""1 stick margarine, melted (1/2 c.)"", ""1 c. sugar"", ""1 tsp. vanilla"", ""2 eggs"", ""6 Tbsp. cocoa"", ""3/4 c. all-purpose flour"", ""1/2 c. pecans (optional)""]"
1629,Grilled Ham Sandwich,"[""1 (3 oz.) pkg. Philadelphia Brand cream cheese, softened"", ""2 tsp. Dijon mustard"", ""1 tsp. Kraft prepared horseradish"", ""1 stick margarine, melted (1/2 c.)"", ""8 whole wheat bread slices"", ""1/2 lb. Velveeta pasteurized process cheese spread, sliced"", ""4 boiled ham slices"", ""soft Parkay margarine""]"
1579,Ground Beef 'N Biscuits,"[""1 1/2 lb. ground beef"", ""1/2 c. chopped onion"", ""2 Tbsp. flour (all-purpose)"", ""1 tsp. salt"", ""1/8 tsp. pepper"", ""1 stick margarine, melted (1/2 c.)"",""1 (15 oz.) can pizza sauce"", ""10 oz. can corn (frozen or canned)"", ""1 tube refrigerated buttermilk biscuits"", ""1 c. (4 oz.) Cheddar cheese, shredded""]"
1549,Buttermilk Pie 1,"[""1/2 stick butter"", ""1 c. sugar"", ""1 Tbsp. flour"", ""1/2 c. chopped onion"", ""3 whole eggs"", ""1/2 c. buttermilk"", ""1 stick margarine, melted (1/2 c.)"",""dash of nutmeg"", ""1 tsp. vanilla"", ""dash of salt"", ""unbaked pie shell""]"
1513,Spaghetti Casserole,"[""1 lb. hamburger"", ""3 onions, chopped"", ""1 small pkg. spaghetti"", ""1/2 c. chopped onion"", ""1 large pkg. cream cheese"", ""1 can tomato soup"", ""1 can milk (empty soup and use can to measure milk)"", ""7 to 8 olives, sliced""]"
1482,Russian Refresher Mix,"[""2 c. powdered orange drink mix"", ""1 (3 oz.) pkg. presweetened lemonade mix"", ""1/2 c. chopped onion"", ""1 1/3 c. sugar"", ""1 tsp. cinnamon"", ""1/2 tsp. ground cloves""]"
1445,Creamy Pasta Salad,"[""8 oz. curly shaped pasta"", ""1 (16 oz.) frozen valley combination vegetables"", ""1/2 c. chopped onion"", ""1 1/2 c. prepared Ranch-style dressing""]"
1409,Microwave Ham Roll-Ups,"[""15 frozen Tater Tots"", ""4 slices Swiss cheese"", ""4 slices boiled ham"", ""1/2 c. chopped onion"", ""1/2 c. sour cream""]"
1371,Open House Salad,"[""1 c. mayo or 1/2 c. mayo and 1/2 c. Miracle Whip"", ""1/4 c. apple cider vinegar"", ""1/2 c. chopped onion"", ""2/3 c. sugar"", ""1/2 c. milk"", ""2 Tbsp. poppy seed"", ""1 head romaine lettuce"", ""1 red onion, sliced"", ""1 pt. strawberries, cut in half""]"
1332,Broccoli Macaroni Casserole,"[""3 Tbsp. butter or margarine"", ""3 Tbsp. flour"", ""1 1/2 tsp. salt"", ""1/2 c. chopped onion"", ""1/8 tsp. pepper"", ""1 1/2 c. milk"", ""3/4 c. mayonnaise"", ""1 3/4 c. macaroni, cooked and drained"", ""2 c. cooked broccoli"", ""1/4 c. grated cheese""]"
1296,Cream Of Spinach Soup,"[""1 1/2 c. frozen leaf spinach, thawed and drained"", ""1 1/4 c. chicken broth"", ""1/2 c. chopped onion"", ""3 Tbsp. margarine"", ""1/4 c. chopped onion"", ""2 Tbsp. flour"", ""1/2 c. whipping cream"", ""dash of pepper"", ""dash of nutmeg""]"
1240,Shoe Peg Corn Casserole,"[""2 cans Shoe Peg corn"", ""2 Tbsp. flour"", ""1/3 c. oleo"", ""3/4 c. half and half"", ""1/2 c. chopped onion"",]"
1183,Carrots A La Orange,"[""1 lb. carrots, sliced diagonally or 1 lb. pkg. frozen carrot slices"", ""2 Tbsp. butter"", ""1 1/2 Tbsp. orange marmalade"", ""pinch of ground nutmeg""]"
1092,Fresh Apple Cake,"[""1 1/4 c. oil"", ""3 eggs"", ""3 c. all-purpose flour"", ""1/2 tsp. salt"", ""3 c. chopped, ""1/2 c. chopped onion"",peeled apples"", ""2 c. sugar"", ""1 Tbsp. vanilla"", ""1 tsp. soda"", ""1 c. chopped pecans""]"
1033,Japanese Fried Rice,"[""1 c. rice (medium grain)"", ""1 lb. ground beef or round steak, cut into small cubes"", ""3 carrots, sliced thin"", ""3 green onions, chopped"", ""salt and pepper to taste"", ""sprinkle of Accent seasoning"", ""soy sauce""]"
None,Mexican Cornbread,"[""2 pkg. Mexican cornbread mix"", ""1 1/2 c. sharp cheese, grated"", ""1 (15 oz.) can creamed corn"", ""1 onion, chopped"", ""1/4 c. oil"", ""1 Tbsp. sugar"", ""1/2 bell pepper, chopped"", ""3 eggs"", ""1 c. buttermilk"", ""4 jalapeno peppers, chopped""]"
None,Guláš (Goulash),"[""1 lb. beef for stew"", ""2 onions, diced"", ""2 cloves of garlic, minced"", ""2 tbsp oil"", ""1 tsp caraway seeds"", ""2 tbsp paprika"", ""salt and pepper to taste"", ""3 potatoes, peeled and diced"", ""1 tbsp flour for thickening""]"
None,Svíčková na smetaně (Beef Sirloin in Cream Sauce),"[""1 kg beef sirloin"", ""2 carrots, diced"", ""1 parsnip, diced"", ""1 celery root, diced"", ""1 onion, diced"", ""3 tbsp oil"", ""1 cup heavy cream"", ""2 tbsp flour"", ""2 tbsp vinegar"", ""1 tsp sugar"", ""salt and pepper""]"
None,Bramboráky (Potato Pancakes),"[""4 large potatoes, grated"", ""2 eggs"", ""4 tbsp flour"", ""3 cloves of garlic, minced"", ""1 tsp marjoram"", ""salt and pepper to taste"", ""oil for frying""]"
None,Vepřo knedlo zelo (Pork with Dumplings and Cabbage),"[""2 lbs pork roast"", ""1 head of cabbage, shredded"", ""1 onion, diced"", ""2 tbsp sugar"", ""2 tbsp vinegar"", ""knedlíky (Czech dumplings)"", ""salt and pepper"", ""caraway seeds"", ""oil""]"
None,Knedlíky (Czech Dumplings),"[""4 cups flour"", ""1 egg"", ""1 cup milk"", ""1 tsp salt"", ""1 tsp baking powder""]"
None,Řízek (Czech Schnitzel),"[""4 pork or chicken cutlets"", ""1 cup flour"", ""2 eggs, beaten"", ""1 cup breadcrumbs"", ""salt and pepper"", ""oil for frying""]"
None,Ovocné Knedlíky (Fruit Dumplings),"[""2 cups flour"", ""1 egg"", ""1 cup milk"", ""1 tbsp sugar"", ""1 tsp salt"", ""fresh fruit (plums, strawberries, etc.)"", ""melted butter"", ""powdered sugar""]"
None,Palačinky (Czech Pancakes),"[""1 cup flour"", ""2 eggs"", ""1 cup milk"", ""1 tbsp sugar"", ""pinch of salt"", ""jam or chocolate spread for filling""]"
None,Zelňačka (Cabbage Soup),"[""1 head of cabbage, shredded"", ""2 potatoes, diced"", ""1 onion, diced"", ""3 cloves of garlic, minced"", ""1 tbsp caraway seeds"", ""1 cup sour cream"", ""2 tbsp flour"", ""salt and pepper"", ""smoked sausage (optional)""]"
None,Tatarák (Steak Tartare),"[""1 lb. beef tenderloin, finely chopped"", ""1 egg yolk"", ""1 onion, finely chopped"", ""2 cloves garlic, minced"", ""2 tbsp mustard"", ""2 tbsp ketchup"", ""1 tbsp paprika"", ""salt and pepper"", ""toast for serving""]"
944,Salmon Casserole Baked In Sour Cream,"[""100 (1 lb.) can salmon, drained and juice reserved"", ""12 Tbsp. lemon juice"", ""12 tsp. salt"", ""pepper to taste"", ""41 c. sour cream"", ""1/2 tsp. dry dill weed"", ""1 medium onion, thinly sliced"", ""1 Tbsp. chopped parsley""]"
943,Bread,"[""22 c. warm water"", ""13 pkg. yeast (RapidRise)"", ""31 Tbsp. melted butter or shortening"", ""12 c. sugar"", ""12 tsp. salt""]"
973,"Slinky(Apple Flavored, Low Calorie Quencher)","[""23 c. sparkling mineral water"", ""2563 c. unsweetened apple juice"", ""123 Tbsp. freshly squeezed lemon juice"", ""a few apple slices and sprig of mint""]"
1021,Broccoli Casserole,"[""233 pkg. frozen broccoli cuts"", ""2 stick butter"", ""123 chopped onion"", ""13 c. cooked rice"", ""233 can cream of mushroom soup"", ""132 small jar Cheez Whiz""]"
1047,Stuffed Cabbage,"[""1/2 medium head cabbage"", ""1/2 onion"", ""1/20 tsp. garlic powder"", ""1/2 tsp. salt"", ""1/3 lb. ground beef"", ""1/4 can sauerkraut"", ""1 can tomato sauce"", ""2 c. water"", ""1 c. instant rice"", ""1 egg"", ""1/2 c. milk""]"
1063,Blueberry Breakfast Bread,"[""2 c. sifted all-purpose flour"", ""1 c. sugar"", ""1 1/2 tsp. baking powder"", ""1/2 tsp. baking soda"", ""1/2 tsp. salt"", ""1 Tbsp. grated orange rind"", ""1 c. grated sharp Cheddar cheese"", ""1 c. frozen dry-packed blueberries"", ""3/4 c. orange juice"", ""2 Tbsp. vegetable oil"", ""1 egg""]"
1078,Christmas All Through The House Potpourri,"[""peel of 1/1 lemon"", ""peel of 1/3 orange"", ""peel of 1/4 grapefruit"", ""1 Tbsp. cloves"", ""1/1 Tbsp. allspice"", ""3 sticks cinnamon""]"
1098,Marshmallows,"[""2 1/4 tbsp. unflavored gelatin"", ""1 1/5 cups granulated sugar"", ""1/8 tsp. salt"", ""2 tbsp. vanilla"", ""1/3 cup light corn syrup"", ""Confectioners sugar for dusting""]"
1122,Fresh Cranberry-Orange Relish,"[""1/2 navel orange, unpeeled and cut into small chunks"", ""1 bag cranberries (2 oz.)"", ""3/8 c. granulated sugar""]"
None,Ragequit Burger,"[""1 stack of salty tears"", ""2 ragequits (freshly harvested)"", ""1 packet of flaming chat logs"", ""3 toxic pings (extra crispy)"", ""1 afk teammate"", ""1 fed enemy champion"", ""salt and pepper to taste"", ""a dash of all-chat banter""]"
None,Int Spaghetti,"[""1 spaghetti strand for each death"", ""a pot of flaming team arguments"", ""3 servings of mispositioning"", ""2 cups of unwarded jungle"", ""1 fed Yasuo"", ""Parmesan cheese for sprinkling (optional)""]"
None,Baron Nashor Salad,"[""1 Baron Nashor"", ""4 clueless teammates"", ""2 overconfident enemies"", ""3 pings on Baron pit"", ""1 failed Smite (well-timed)"", ""a sprinkle of FF votes""]"
None,ARAM Ice Cream,"[""1 random champion you’ve never played"", ""3 questionable builds"", ""a pinch of no boots"", ""5 items of full AP on a tank"", ""an infinite scoop of laughter""]"
None,Flash Ignite Nachos,"[""1 poorly timed Flash"", ""1 unnecessary Ignite"", ""2 cups of cheese (for the chat)"", ""1 packet of Doritos"", ""1 epic fail moment""]"
None,Tilt Tacos,"[""3 taco shells"", ""a handful of tilted players"", ""1 fed Teemo"", ""a pinch of passive aggression"", ""5 pings (for seasoning)"", ""hot sauce made from elo tears""]"
None,Overstay Soup,"[""1 teamfight victory"", ""2 unnecessary tower dives"", ""a quart of overstaying"", ""3 pings for retreat"", ""1 Baron throw"", ""teammates yelling 'back!'""]"
None,Toxicity Tart,"[""1 serving of passive-aggressive chat"", ""3 poorly aimed skill shots"", ""5 sarcastic 'gj' comments"", ""2 missed objectives"", ""a spoonful of report threats"", ""sugar to disguise toxicity (optional)""]"
None,Overfed Steak,"[""1 enemy ADC with 20 kills"", ""3 cups of misplays"", ""1 tank who forgot to build tank items"", ""2 supports per team"", ""salt from chat"", ""a splash of surrender votes""]"
None,FF@15 Smoothie,"[""1 blender of tilted vibes"", ""2 scoops of 'ff@15' pings"", ""1 early game throw"", ""a dash of AFK energy"", ""garnish with muted players""]"
"""

import re

# Usuwanie wszystkiego do drugiego przecinka i czyszczenie danych
cleaned_data = re.sub(r'^[^,]*,[^,]*,', '', data, flags=re.M)  # Usuwanie numeru i tytułu przepisu
cleaned_data = re.sub(r'[\"\[\]]', '', cleaned_data)  # Usuwanie cudzysłowów i nawiasów

print(cleaned_data)
