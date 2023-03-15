import streamlit as st

html_temp = """
<div style="background-color:#748c08;padding:1.5px">
<h1 style="color:white;text-align:center;">10 Exercises for Diabetes 🚴</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.header('1. Walking')
st.markdown('You don’t need a gym membership or expensive exercise equipment to get moving.')
st.markdown('If you have a supportive pair of shoes and a safe place to walk, you can start today. In fact, you can meet your recommended minimum target for aerobic fitness by going for a brisk 30-minute walk five days per week.')
st.markdown('According to a 2023 review, walking can help people with type 2 diabetes lower their blood pressure, HbA1c levels, and body mass index.')

st.header('2. Cycling')
st.markdown('Roughly half of people with type 2 diabetesTrusted Source have arthritis. The two conditions have several risk factors in common, including obesity.')
st.markdown('Diabetic neuropathy, a condition that occurs when the nerves become damaged, can also cause joint pain in people with type 2 diabetes.')
st.markdown('If you have lower joint pain, consider choosing low impact exercise. Cycling, for example, can help you meet your fitness goals while minimizing strain on your joints.')

st.header('3. Swimming')
st.markdown('Aquatic activities provide another joint-friendly exercise option. For example, swimming, water aerobics, aqua jogging, and other aquatic activities can give your heart, lungs, and muscles a workout, while putting little stress on your joints.')
st.markdown('A 2017 reviewTrusted Source found that aquatic exercise can help lower blood sugar levels, much like land based exercise does.')

st.header('4. Team sports')
st.markdown('If you find it hard to motivate yourself to exercise, it might help to join a recreational sports team. The opportunity to socialize with teammates and the commitment you make to them might help you find the motivation you need to show up each week.')
st.markdown('Many recreational sports offer a good aerobic workout. Consider trying basketball, soccer, softball, pairs tennis, or ultimate frisbee.')

st.header('5. Aerobic dance')
st.markdown('Signing up for an aerobic dance or other fitness class might also help you meet your exercise goals. For instance, Zumba is a fitness program that combines dance and aerobic movements for a fast-paced workout.')
st.markdown('A 2015 studyTrusted Source found that women with type 2 diabetes were more motivated to exercise after taking part in Zumba classes for 16 weeks. Participants also improved their aerobic fitness and lost weight.')

st.header('6. Weightlifting')
st.markdown('Weightlifting and other strengthening activities help build your muscle mass, which can increase the number of calories you burn each day. Strength training may also help improve your blood sugar control, according to the ADA.')
st.markdown('If you want to incorporate weightlifting into your weekly exercise routine, you can use weight machines, free weights, or even heavy household objects, such as canned goods or water bottles.')
st.markdown('To learn how to lift weights safely and effectively, consider joining a weightlifting class or asking a professional fitness trainer for guidance.')

st.header('7. Resistance band exercises')
st.markdown('Weights aren’t the only tool you can use to strengthen your muscles. You can also perform a wide variety of strengthening activities with resistance bands.')
st.markdown('To learn how to incorporate them into your workouts, speak with a professional trainer, take a resistance band class, or watch a resistance band workout video.')
st.markdown('In addition to increasing your strength, exercising with resistance bands may provide modest benefits to your blood sugar control, according to a 2018 study.')

st.header('8. Calisthenics')
st.markdown('In calisthenics, you use your own bodyweight to strengthen your muscles. Common calisthenic exercises include pushups, pullups, squats, lunges, and abdominal crunches.')
st.markdown('Whether you choose to strengthen your muscles with weights, resistance bands, or your own body weight, try to work out every major muscle group in your body.')
st.markdown('To give your body time to recover, experts suggest taking a day off from muscle-strengthening activities between each session of strength training.')

st.header('9. Pilates')
st.markdown('Pilates is a popular fitness program that’s designed to improve core strength, coordination, and balance. According to a 2020 study of older adult women with type 2 diabetes, it may also help improve blood sugar control.')
st.markdown('Consider signing up for a Pilates class at your local gym or Pilates studio. Many instructional videos and books are also available.')

st.header('10. Yoga')
st.markdown('According to a 2016 review, yoga can help people with type 2 diabetes manage their blood sugar, cholesterol levels, and weight. It might also help lower your blood pressure, improve the quality of your sleep, and boost your mood.')
st.markdown('If you’re interested in trying yoga, sign up for a class at a local studio or gym. A trained professional can help you learn how to move from one pose to another, using the proper posture and breathing technique.')



