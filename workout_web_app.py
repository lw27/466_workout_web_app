# Version Python 3.7
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_index():
    return """
    <html>
    <title>Home - Workout App</title>
    <head>
    <style>
    ul
    {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #009933;
    }

    li
    {
        float: left;
    }
    
    li a
    {
        display: block;
        color: white;
        text-align: center;
        padding: 16px;
        text-decoration: none;
    }

    li a:hover
    {
        background-color: #33ff77;
    }
    </style>
    </head>

    <body>
    <h2>Home Navigation Page</h2>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/premade_workouts">Workouts</a></li>
    <li><a href="/premade_meal_plans">Meal Plans</a></li>
    <li><a href="/tools">Tools</a></li>
    <li><a href="/about">About</a></li>
    </ul>
    </body>
    </html>
    """

@app.route('/premade_workouts')
def premade_workouts():
    return """
    <html>
    <title>Premade Workouts</title>
    <h1>Hello! Welcome to the Premade Workouts Page.</h1>
    <p>Pick your Workouts!</p>
    <ul>
        <li><a href="/warm_up">Warm Up</a></li>
        <li><a href="/build_total_body_strength">Build Total-Body Strength</a></li>
        <li><a href="/train_your_body_in_5_minutes">Train Your Body in 5 Minutes</a></li>
        <li><a href="/improve_your_endurance">Improve Your Endurance</a></li>
    <p>Pick your Workout Playlist!</p>
        <li><a href="https://www.youtube.com/watch?v=sdtX44n4-lc&list=PLChOO_ZAB22WAvnFw86vUueyv026ULwIv&index=4">Hip-Hop</a></li>
        <li><a href="https://www.youtube.com/watch?v=o3WdLtpWM_c&list=PLMmqTuUsDkRINEEFXWy7Ne2897vCdxJg1">Techno</a></li>
        <li><a href="https://www.youtube.com/watch?v=eJnQBXmZ7Ek&list=PL8fAVuusm10qMUzauh8UoYkzrRHO0KU1z">Rock</a></li>
        <li><a href="https://www.youtube.com/watch?v=VkloKZmQ3o4&list=PL6s8R-CiO2_zB85o0H4PSZeebk5P-PUWx">Country</a></li>
        <li><a href="https://www.youtube.com/watch?v=Tztc73r8348&list=PLChOO_ZAB22WuyDODJ3kjJiU0oQzWOTyb">Pop</a></li>
        <li><a href="https://www.youtube.com/watch?v=DNobqcfLb2Y&list=PLxvodScTx2RsV2VIDIBksBmuLFngu3mgU">Reggae</a></li>
        <li><a href="https://www.youtube.com/watch?v=FEAZyRfgevc">EDM</a></li>
        <li><a href="https://www.youtube.com/watch?v=EFJ7kDva7JE&list=PLxvodScTx2RtAOoajGSu6ad4p8P8uXKQk">Classical</a></li>
    </ul>
    <a href="/">Back to homepage</a>
    <h6>©All Rights reserved by original authors.</h6>
    </html>
    """

@app.route('/premade_meal_plans')
def meal_plans():
    return """
    <html>
    <title>Premade Meal Plans</title>
    <h1>Hello! Welcome to the Premade Meal Plans Page.</h1>
    <p>Pick your Meal plans!</p>
    <ul>
        <li><a href="/the_beginner_meal_plan">The Beginner Meal Plan</a></li>
        <li><a href="/the_get-lean_meal_plan">The Get-Lean Meal Plan</a></li>
        <li><a href="/the_skinny_guy_muscle-gain_plan">The Skinny Guy Muscal-Gain Plan</a></li>
    </ul>
    <a href="/">Back to homepage</a>
    <h6>©All Rights reserved by original authors.</h6>
    </html>
    """

# Workouts start here.
@app.route('/warm_up')
def warm_up():
    return """
    <html>
    <title>Premade Workouts</title>
    <h3>You can pick the following exercises: </h3>
    <ul>
        <li><a href="https://www.ideafit.com/exercise-library/glute-bridge-marching">glute bridge - marching</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/internal-and-external-hip-rotation-prone">internal and external hip rotation - prone</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/knee-hug-to-forward-lunge-elbow-to-instep">knee hug to forward lunge, elbow to instep</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/leg-overs-alternating">leg overs - alternating</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/knee-hug-moving-forward">knee hug - moving forward</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/reverse-lunge-with-rotation">reverse lunge - with rotation</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/drop-lunge-alternating-sides">drop lunge - alternating sides</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/lateral-squat-low">lateral squat - low</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/inverted-hamstring-moving-forward">inverted hamstring moving forward</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/heel-to-glute-with-arm-reach-contra">heel to glute - with arm reach (contra)</a></li>
    </ul>
    <a href="/premade_workouts">Back to previous page</a>
    <br><a href="/">Back to homepage</a>
    <h6>©All Rights reserved by original authors.</h6>
    </html>
    """

@app.route('/build_total_body_strength')
def build_total_body_strength():
    return """
    <html>
    <title>Premade Workouts</title>
    <h3>You can pick the following exercises: </h3>
    <ul>
        <li><a href="https://www.ideafit.com/exercise-library/inverted-hamstring-in-place-with-arm-reach">inverted hamstring - in place with arm reach</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/knee-hug-moving-forward">knee hug - moving forward</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/lateral-squat-low">lateral squat - low</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/forward-lunge-elbow-to-instep-kneeling-in-place">forward lunge, elbow to instep - kneeling in place</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/bench-press-alternating-dumbbell">bench press - alternating dumbbell</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/romanian-deadlift-1-leg-dumbbell">romanian deadlift - 1 leg dumbbell</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/squat-to-press-dumbbell">squat to press - dumbbell</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/rotational-lift-standing-cable-rope">rotational lift - standing cable (rope)</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/curl-to-overhead-press-front-foot-elevated-dumbbell">curl to overhead press - front foot elevated dumbbell</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/lateral-dynamic-pillar-bridge-feet-stacked">lateral dynamic pillar bridge - feet stacked</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/lateral-lunge-slide">lateral lunge (slide)</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/bent-over-row-1-arm-1-leg-dumbbell-contra">bent over row - 1 arm 1 leg dumbbell (contra)</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/rotational-crunch-stability-ball">rotational crunch (stability ball)</a></li>
    </ul>
    <a href="/premade_workouts">Back to previous page</a>
    <br><a href="/">Back to homepage</a>
    <h6>©All Rights reserved by original authors.</h6>
    </html>
    """

@app.route('/train_your_body_in_5_minutes')
def train_your_body_in_5_minutes():
    return """
    <html>
    <title>Premade Workouts</title>
    <h3>You can pick the following exercises: </h3>
    <ul>
        <li><a href="https://www.ideafit.com/exercise-library/heel-to-glute-moving-forward-with-arm-reach-ipsi">heel to glute - moving forward with arm reach (ipsi)</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/forward-lunge-elbow-to-instep-crawling">forward lunge, elbow to instep - crawling</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/handwalk-moving-backward">handwalk - moving backward</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/lateral-lunge-0">lateral lunge</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/push-up-2">push up</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/pillar-bridge-with-arm-lift">pillar bridge - with arm lift</a></li>
    </ul>
    <a href="/premade_workouts">Back to previous page</a>
    <br><a href="/">Back to homepage</a>
    <h6>©All Rights reserved by original authors.</h6>
    </html>
    """

@app.route('/improve_your_endurance')
def improve_your_endurance():
    return """
    <html>
    <title>Premade Workouts</title>
    <h3>You can pick the following exercises: </h3>
    <ul>
        <li><a href="https://www.ideafit.com/exercise-library/inverted-hamstring-in-place-with-arm-reach">inverted hamstring - in place with arm reach</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/knee-hug-moving-forward">knee hug - moving forward</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/reverse-lunge-with-lateral-flexion-0">reverse lunge - with lateral flexion</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/pillar-bridge">pillar bridge</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/lateral-pillar-bridge-feet-stacked">lateral pillar bridge - feet stacked</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/glute-bridge-marching">glute bridge - marching</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/mini-band-external-rotation">mini band - external rotation</a></li>
        <li><a href="https://www.ideafit.com/exercise-library/ys-floor-0">ys - floor</a></li>
    </ul>
    <a href="/premade_workouts">Back to previous page</a>
    <br><a href="/">Back to homepage</a>
    <h6>©All Rights reserved by original authors.</h6>
    </html>
    """

# Meal Plans start here.
@app.route('/the_beginner_meal_plan')
def the_beginner_meal_plan():
    # source: https://www.bodybuilding.com/content/meal-plan-for-every-guy.html
    return """
    <html>
    <title>Premade Meal Plans</title>
    <body>
        <h2>The Beginner Meal Plan</h2>
        <dl>
            <dt><strong>Target:</strong></dt>
            <dd>- 2,500 calories</dd>
            <dd>- 218g carbs</dd>
            <dd>- 218g protein</dd>
            <dd>- 83g fat</dd>
        </dl>

        <h3>Sample Meal Options</h3>
        <dl>
            <dt><strong>Meal 1:</strong></dt>
            <dd>- Greek Yogurt: 1 and 1/2 cups</dd>
            <dd>- Raspberries: 1/2 cup</dd>
            <dd>- Granola: 1/3 cup </dd>
            <dd>- Eggs: 3</dd>
            <dd><li><strong>Raspberry Alternate Options: </strong>5 sliced strawberries, 1/2 cup blueberries, 2/3 cup blackberries, or 1 tbsp raisins</li></dd>
            <dd><li><strong>Granola Alternate Options: </strong>1/3 cup Ezekiel Cinnamon Raisin cereal, 1/3 cup rolled oats, 3/4 cup Fiber One cereal, or 2/3 cup Kashi Organic Cinnamon Harvest</li></dd>
            <br>

            <dt><strong>Meal 2: Double Chocolate Cherry Smoothie</strong></dt>
            <dd>- Protein Powder (Chocolate): 2 scoops</dd>
            <dd>- Coconut Milk: 1/4 cup</dd>
            <dd>- Cherries: 3/4 cup </dd>
            <dd>- Flaxseeds: 1 tbsp</dd>
            <dd>- Cocoa Powder: 1 tbsp</dd>
            <dd>- Ice: 3-4 cubes</dd>
            <dd>- Water: 2-3 cups</dd>
            <dd><li><strong>Coconut Milk Alternate Options: </strong>2 tbsp chopped walnuts</li></dd>
            <dd><li><strong>Cherries Alternate Options: </strong>1 cup blackberries</li></dd>
            <br>

            <dt><strong>Meal 3: Bibb Lettuce Burger</strong></dt>
            <dd>- Lettuce: 2 leaves</dd>
            <dd>- Ground Beef (95% lean): 8 oz.</dd>
            <dd>- Tomato: 2 slices </dd>
            <dd>- Red Onion: 2 slices</dd>
            <dd>- Ketchup: 1 tbsp</dd>
            <dd>- Mayonnaise: 1 tbsp</dd>
            <dd>- Green Beans: 3 cups</dd>
            <br>

            <dt><strong>Meal 4: Post-Workout Nutrition</strong></dt>
            <dd>- Protein Bar (or Recovery shake): 1 serving</dd>
            <br>

            <dt><strong>Meal 5: Shrimp with Spinach Salad & Brown Rice</strong></dt>
            <dd>- Shrimp: 6 oz.</dd>
            <dd>- Brown Rice: 1/4 cup</dd>
            <dd>- Spinach: 4 cups</dd>
            <dd>- Feta Cheese: 1/4 cup</dd>
            <dd>- Bell Pepper: 1/2</dd>
            <dd>- Olive Oil (Extra virgin): 2 tbsp</dd>
        </dl>
        <a href="/premade_meal_plans">Back to previous page</a>
        <br><a href="/">Back to homepage</a>
        <h6>©All Rights reserved by original authors.</h6>
    </body>
    </html>
    """

@app.route('/the_get-lean_meal_plan')
def the_get_lean_meal_plan():
    # source: https://www.bodybuilding.com/content/meal-plan-for-every-guy.html
    return """
    <html>
    <title>Premade Meal Plans</title>
    <body>
        <h2>The Get-Lean Meal Plan</h2>
        <dl>
            <dt><strong>Target:</strong></dt>
            <dd>- 2,000 calories</dd>
            <dd>- 150g carbs</dd>
            <dd>- 150g protein</dd>
            <dd>- 88g fat</dd>
        </dl>

        <h3>Sample Meal Options</h3>
        <dl>
            <dt><strong>Meal 1: Spinach Omelet</strong></dt>
            <dd>- Eggs: 3</dd>
            <dd>- Cheese (Pepper jack): 1 slice</dd>
            <dd>- Spinach (Baby spinach): 1 cup </dd>
            <dd>- Peach: 1</dd>
            <br>

            <dt><strong>Meal 2: Chocolate Nut Shake</strong></dt>
            <dd>- Protein Powder (Chocolate): 1 scoop</dd>
            <dd>- Chocolate Milk: 2 cups</dd>
            <dd>- Peanut Butter: 2 tbsp </dd>
            <dd>- Chia Seeds: 1 tbsp</dd>
            <dd>- Ice: 2-3 cubes</dd>
            <br>

            <dt><strong>Meal 2 Alternative: Strawberry Cream Smoothie</strong></dt>
            <dd>- Protein Powder (Vanilla): 1 scoop</dd>
            <dd>- Flaxseeds: 1 tbsp</dd>
            <dd>- Strawberies: 6</dd>
            <dd>- Yogurt: 3/4 cup</dd>
            <br>

            <dt><strong>Meal 3: Grilled Steak with Avocado-Tomato Salad</strong></dt>
            <dd>- Steak (Top round): 4 oz.s</dd>
            <dd>- Avocado: 1/2</dd>
            <dd>- Tomato: 1 </dd>
            <br>

            <dt><strong>Meal 4: Post-Workout Nutrition</strong></dt>
            <dd>- Protein Powder (or Recovery shake. Should contain 50g carbs and 25g protein): 1 serving</dd>
            <br>

            <dt><strong>Meal 5: Flax Pasta with Hearty Sauce</strong></dt>
            <dd>- Chicken (chicken breast): 3 oz.</dd>
            <dd>- Pasta (Whole-wheat flax penne pasta): 1 oz.</dd>
            <dd>- Mushrooms (Sliced): 1 cups</dd>
            <dd>- Broccoli (Florets): 2 cups</dd>
            <dd>- Marinarry Sauce: 1/2 cup</dd>
            <dd>- Olive Oil (Extra virgin): 1 tbsp</dd>
            <dd><li><strong>Chicken Alternate Options: </strong>3 oz. 95% lean ground beef, 3 oz yellowfin tuna, 5 oz clams, or 3 oz clod roast</li></dd>
            <dd><li><strong>Mushrooms Alternate Options: </strong>3 stalks asparagus, 1 cup chopped baby spinach, 3 baby zucchini, or 1 diced plum tomato</li></dd>
            <dd><li><strong>Broccoli Alternate Options: </strong>2 cups cubed eggplant, 1 diced yellow pepper or summer squash, or 1 diced carrot + 1 diced stalk of celery</li></dd>
        </dl>
        <a href="/premade_meal_plans">Back to previous page</a>
        <br><a href="/">Back to homepage</a>
        <h6>©All Rights reserved by original authors.</h6>
    </body>
    </html>
    """

@app.route('/the_skinny_guy_muscle-gain_plan')
def the_skinny_guy_muscle_gain_plan():
    # source: https://www.bodybuilding.com/content/meal-plan-for-every-guy.html
    return """
    <html>
    <title>Premade Meal Plans</title>
    <body>
        <h2>The Skinny Guy Muscle-Gain Plan</h2>
        <dl>
            <dt><strong>Target:</strong></dt>
            <dd>- approx. 3,000 calories</dd>
            <dd>- 300g carbs</dd>
            <dd>- 225g protein</dd>
            <dd>- 100g fat</dd>
        </dl>

        <h3>Sample Meal Options</h3>
        <dl>
            <dt><strong>Meal 1: Cheesy Scrambled Eggs with Scallions</strong></dt>
            <dd>- Eggs: 3</dd>
            <dd>- Egg Whites: 4</dd>
            <dd>- Cheese (Cheddar): 1/4 cup </dd>
            <dd>- Scallions: 2</dd>
            <dd>- Ezekiel Bread: 2 slices</dd>
            <dd>- Apple: 1</dd>
            <dd><li><strong>Egg Whites Alternate Options: </strong>2 slices turkey bacon, 2 small chicken sausages, 2 slices Canadian bacon, or 1/4 cup canned salmon</li></dd>
            <dd><li><strong>Scallions Alternate Options: </strong>2 tbsp salsa, 1/4 cup diced onions, or 2 tbsp diced sun-dried tomatoes</li></dd>
            <br>

            <dt><strong>Meal 2: Blueberry Almond Smoothie</strong></dt>
            <dd>- Protein Powder (Vanilla): 2 scoop</dd>
            <dd>- Blueberries: 1 cup</dd>
            <dd>- Alomonds: 1 oz. </dd>
            <dd>- Almond Milk (Vanilla): 1 cup</dd>
            <dd>- Water: 1 cup</dd>
            <dd>- Ice: 3-4 cubes</dd>
            <dd><li><strong>Buleberries Alternate Options: </strong>3/4 cup frozen mango chunks</li></dd>
            <br>

            <dt><strong>Meal 3: Steak with Tomato Bean Salad</strong></dt>
            <dd>- Steak (Grilled flank steak): 6 oz.s</dd>
            <dd>- Tomato: 1 </dd>
            <dd>- Cucumber (Diced): 1/2 </dd>
            <dd>- Chickpeas: 1 cup</dd>
            <dd>- Olive Oil: 1 tbsp</dd>
            <br>

            <dt><strong>Meal 4: Post-Workout Nutrition</strong></dt>
            <dd>- Protein Powder (or Recovery shake. Should contain 50g carbs and 25g protein): 1 serving</dd>
            <br>

            <dt><strong>Meal 5: Chicken with Quinoa Salad</strong></dt>
            <dd>- Chicken Breast: 6 oz.</dd>
            <dd>- Quinoa: 1/3 cup</dd>
            <dd>- Walnutes: 2 tbsp</dd>
            <dd>- Craisins: 2 tbsp</dd>
            <dd><li><strong>Chicken Breast Alternate Options: </strong>6 oz pork tenderloin, 5 oz Buffalo rib eye, or 5 oz top round beef</li></dd>
            <dd><li><strong>Quinoa Alternate Options:: </strong>1/3 cup couscous, 1/4 cup brown rice, or 1/4 cup wild rice</li></dd>
            <br>

            <dt><strong>Meal 6: Yams and Parmesan White Fish</strong></dt>
            <dd>- Tilapia: 6 oz.</dd>
            <dd>- Parmesan Cheese: 2 tbsp</dd>
            <dd>- Yams: 2 medium</dd>
            <dd>- Butter: 1 tbsp</dd>
            <dd>- Broccoli: 1 cup</dd>
            <dd><li><strong>Tilapia Alternate Options: </strong>5 oz tuna steak, 7 oz cod, or 6 oz shrimp</li></dd>
            <dd><li><strong>Yams Alternate Options: </strong>1/3 cup Amaranth, 1/3 cup wheat berries, or 1/3 cup pearl barley</li></dd>
        </dl>
        <a href="/premade_meal_plans">Back to previous page</a>
        <br><a href="/">Back to homepage</a>
        <h6>©All Rights reserved by original authors.</h6>
    </body>
    </html>
    """

@app.route('/tools')
def tools():
    return """
    <html>
    <title>Tools</title>
    <h1>Put links of tools.</h1>
    <a href="/">Back to homepage</a>
    </html>
    """

@app.route('/about')
def about():
    return """
    <html>
    <title>About This App</title>
    <h1>Insert App Description.</h1>
    <a href="/">Back to homepage</a>
    </html>
    """
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
