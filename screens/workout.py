import customtkinter as ctk
from tkinter import messagebox, filedialog
from tkinter.ttk import Label
import os
from PIL import Image, ImageTk
import random
from tkinter import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def open_work():
    from screens.selection import Shared
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    win = ctk.CTk()
    win.title("WORKOUT")
    win.geometry("1200x800")
    canvas = Canvas(win, width=500, height=300, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def draw_gradient(canvas, color1, color2):
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        r1, g1, b1 = win.winfo_rgb(color1)
        r2, g2, b2 = win.winfo_rgb(color2)

        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height

        for i in range(height):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))

            hex_color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'

            canvas.create_line(0, i, width, i, fill=hex_color)
    def update_gradient(event):
        canvas.delete("all")
        draw_gradient(canvas, "#06193b", "#344b73")  
    

    canvas.bind("<Configure>", update_gradient)

    Jumping_Jacks = ["JUMPING JACKS", "Stand straight with feet together and arms by your side. Jump up, spreading your feet shoulder-width apart while raising your arms overhead. Return to start and repeat steadily."]

    Arm_Swings = ["ARM SWINGS", "Stand tall and swing your arms forward and backward in a controlled motion to loosen shoulder joints."]

    Hip_Circles = ["HIP CIRCLES", "Place hands on hips and rotate them in large circles clockwise and anticlockwise for even mobility."]

    Leg_Swings = ["LEG SWINGS", "Hold onto a wall or chair for balance. Swing one leg forward and backward, then side to side. Switch legs."]

    Torso_Twists = ["TORSO TWISTS", "Stand with feet shoulder-width apart, hands at chest level, and rotate your torso left and right smoothly."]

    High_Knees = ["HIGH KNEES", "Run in place bringing your knees up to waist level. Keep your core tight and back straight."]

    Lunges_with_Rotation = ["LUNGES WITH ROTATION", "Step forward into a lunge, twist your torso toward the front leg, then return to standing. Alternate sides."]

    Skater_Steps = ["SKATER STEPS", "Hop from side to side, crossing one leg behind the other while swinging arms naturally."]

    Inchworms = ["INCHWORMS", "Bend at your hips, touch the floor, and walk your hands forward to a plank. Hold for a moment, then walk your hands back and stand up."]

    Mountain_Climbers = ["MOUNTAIN CLIMBERS", "Start in plank position and drive one knee toward your chest, then quickly switch legs as if running horizontally."]

    Burpees = ["BURPEES", "From standing, squat down, kick your legs back to a plank, do a push-up, jump back to squat, and explode up with a jump."]

    Jump_Squats = ["JUMP SQUATS", "Perform a regular squat and then jump explosively, landing softly and going right back into the next rep."]

    Running_in_Place = ["RUNNING IN PLACE", "Run with high knees and quick footwork, staying light on your toes."]

    Butt_Kicks = ["BUTT KICKS", "Jog in place and bring your heels up to hit your glutes with each step."]

    High_Knees_2 = ["HIGH KNEES", "Run in place, driving knees toward your chest quickly while pumping your arms."]

    Skater_Jumps = ["SKATER JUMPS", "Leap sideways from one leg to the other, like a speed skater, keeping your core engaged."]

    Jump_Rope = ["JUMP ROPE", "Pretend to skip or use a rope. Stay light on your feet and keep elbows close to your torso."]

    Box_Jumps = ["BOX JUMPS", "Stand in front of a sturdy box or bench. Jump up onto it with both feet, land softly, and step down carefully."]

    Plank_Jacks = ["PLANK JACKS", "Start in plank position. Jump both feet out wide, then back together, while keeping your upper body steady."]

    Push_Ups = ["PUSH-UPS", "Start in plank position, hands shoulder-width apart. Lower your chest until it nearly touches the floor, then push back up."]

    Squats = ["SQUATS", "Stand with feet shoulder-width apart, push hips back, bend knees, and lower until thighs are parallel to floor. Return to standing."]

    Lunges = ["LUNGES", "Step forward with one leg and lower until both knees are at 90°. Push back to start and repeat on the other leg."]

    Plank_Shoulder_Taps = ["PLANK SHOULDER TAPS", "In a plank, tap your left shoulder with your right hand, then right shoulder with left hand while keeping hips steady."]

    Glute_Bridges = ["GLUTE BRIDGES", "Lie on your back, knees bent. Lift hips upward by squeezing glutes, hold briefly, then lower down."]

    Tricep_Dips = ["TRICEP DIPS", "Sit on a bench or chair edge. Place hands beside hips, slide off, and lower your body until elbows are at 90°, then push back up."]

    Bicycle_Crunches = ["BICYCLE CRUNCHES", "Lie flat, hands behind head. Alternate touching each elbow to the opposite knee in a cycling motion."]

    Wall_Sit = ["WALL SIT", "Sit against a wall with knees bent at 90°, back straight, and hold the position for as long as you can."]

    Superman_Hold = ["SUPERMAN HOLD", "Lie on your stomach, extend arms and legs, and lift them off the ground. Hold for a few seconds, then lower."]

    Side_Plank = ["SIDE PLANK", "Lie on your side, propped up on one elbow, and lift hips to form a straight line from head to feet. Hold and switch."]
    Dumbbell_Squats = ["DUMBBELL SQUATS", "Hold dumbbells by your sides, keep your back straight, sit like on a chair, and stand back up to strengthen thighs, glutes, and core."]

    Resistance_Band_Rows = ["RESISTANCE BAND ROWS", "Hook the band to a door or pole and pull both ends toward your chest while squeezing your shoulder blades to work your upper back and arms."]

    Kettlebell_Swings = ["KETTLEBELL SWINGS", "Swing a kettlebell from between your legs to chest height using your hips to train legs, glutes, and cardio."]

    Barbell_Bench_Press = ["BARBELL BENCH PRESS", "Lie on a bench and push the barbell upward, then lower it slowly to build chest, shoulders, and triceps."]

    Medicine_Ball_Slams = ["MEDICINE BALL SLAMS", "Lift a medicine ball overhead and slam it to the floor, then squat to pick it up, working core, shoulders, and power."]

    Cable_Chest_Fly = ["CABLE CHEST FLY", "Stand between cable handles and pull them forward in a hugging motion to work the chest and shoulders."]

    Leg_Press = ["LEG PRESS", "Sit on the machine, place your feet on the platform, and push it away by straightening your legs to target thighs, hamstrings, and glutes."]

    Lat_Pulldown = ["LAT PULLDOWN", "Hold the overhead bar and pull it down to your chest to strengthen your upper back and arms."]

    Weighted_Step_Ups = ["WEIGHTED STEP-UPS", "Hold dumbbells and step onto a bench one leg at a time to train legs, glutes, and balance."]

    Battle_Rope_Waves = ["BATTLE ROPE WAVES", "Hold battle ropes and move your arms up and down to create waves for arms, shoulders, and cardio endurance."]

    Downward_Dog = ["DOWNWARD DOG", "Start on all fours, lift hips up and back, forming an inverted V shape. Keep heels pressing toward the ground and spine long."]

    Cobra_Pose = ["COBRA POSE", "Lie on your stomach, place palms under shoulders, and lift your chest while keeping hips on the mat."]

    Childs_Pose = ["CHILD’S POSE", "Sit back on heels, stretch arms forward on the floor, and relax your forehead to the mat."]

    Warrior_II = ["WARRIOR II", "Step one foot forward, bend the front knee, and stretch arms parallel to the floor. Gaze over front hand."]

    Cat_Cow = ["CAT-COW", "On hands and knees, alternate arching and rounding your back slowly to loosen your spine."]

    Bridge_Pose = ["BRIDGE POSE", "Lie on your back, bend knees, lift hips, and clasp hands beneath you for a chest and glute opener."]

    Triangle_Pose = ["TRIANGLE POSE", "Step your feet apart, extend one arm toward the sky, and lean sideways over your front leg."]

    Seated_Forward_Bend = ["SEATED FORWARD BEND", "Sit with legs straight, bend forward from your hips, and reach toward your toes."]

    Tree_Pose = ["TREE POSE", "Stand on one leg, place the other foot on the inner thigh, and bring palms together in front of your chest."]

    Pigeon_Pose = ["PIGEON POSE", "From plank, bring one knee forward and lay it across the mat while extending the other leg behind you. Hold to open hips."]

    all_warmup = []
    all_cardio = []
    all_yoga = []
    
    duration = Shared.clicked1
    intensity = Shared.clicked2
    eqp = Shared.clicked3

    def workout_selection():
        def finish_workout():
            messagebox.showinfo("Workout Completed", "FINISHED WORKOUT")
            win.destroy()
        def timer(timer_seconds,is_running,timer_label,result_frame,timer_time):
            def countdown():
                if not is_running[0]:
                    return   

                mins = timer_seconds[0] // 60
                secs = timer_seconds[0] % 60
                timer_label.configure(text=f"{mins}:{secs:02d}")

                if timer_seconds[0] > 0:
                    timer_seconds[0] -= 1
                    result_frame.after(1000, countdown)
                else:
                    timer_label.configure(text="Time’s Up!")

            def start_timer():
                if not is_running[0]:
                    timer_seconds[0] = timer_time   
                    is_running[0] = True
                    countdown()

            def pause_timer():
                is_running[0] = False

            def resume_timer():
                if not is_running[0] and timer_seconds[0] > 0:
                    is_running[0] = True
                    countdown()

            start_btn = ctk.CTkButton(result_frame, text="Start",fg_color="#4a90e2",
        hover_color="#357ABD", command=start_timer)
            start_btn.pack(pady=5)

            pause_btn = ctk.CTkButton(result_frame, text="Pause", fg_color="#4a90e2",
        hover_color="#357ABD",command=pause_timer)
            pause_btn.pack(pady=5)

            resume_btn = ctk.CTkButton(result_frame, text="Resume",fg_color="#4a90e2",
        hover_color="#357ABD", command=resume_timer)
            resume_btn.pack(pady=5)
        
        def finish_and_save_pdf(all_warmup, all_cardio, all_yoga):
            answer = messagebox.askyesno(
                "Save Workout?",
                "Do you want to save your workout summary as a PDF?" )
            if not answer:
                messagebox.showinfo("Skipped", "Workout summary was not saved.")
                win.destroy()
                return
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF Files", "*.pdf")], title="Save Workout Summary As",initialfile="workout_summary.pdf")

            if not file_path:
                messagebox.showinfo("Cancelled", "File not saved.")
                win.destroy()
                return
            

            pdf = SimpleDocTemplate(file_path, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            story.append(Paragraph("<b>Your Workout Summary</b>", styles["Title"]))
            story.append(Spacer(1, 20))


            story.append(Paragraph("<b>Warmup Exercises:</b>", styles["Heading2"]))
            for ex in all_warmup:
                name = ex[0]
                desc = ex[1]
                story.append(Paragraph(f"<b>{name}</b><br/>{desc}", styles["BodyText"]))
                story.append(Spacer(1, 6))
            story.append(Spacer(1, 12))

            story.append(Paragraph("<b>Cardio Exercises:</b>", styles["Heading2"]))
            for ex in all_cardio:
                name = ex[0]
                desc = ex[1]
                story.append(Paragraph(f"<b>{name}</b><br/>{desc}", styles["BodyText"]))
                story.append(Spacer(1, 6))
            story.append(Spacer(1, 12))

            story.append(Paragraph("<b>Yoga Exercises:</b>", styles["Heading2"]))
            for ex in all_yoga:
                name = ex[0]
                desc = ex[1]
                story.append(Paragraph(f"<b>{name}</b><br/>{desc}", styles["BodyText"]))
                story.append(Spacer(1, 6))
            story.append(Spacer(1, 12))

            pdf.build(story)

            messagebox.showinfo("Saved", f"Workout summary saved:\n{file_path}")
            win.destroy()
        
        if duration == "30" and intensity == "EASY" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)

                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)

                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)

                    next_button = ctk.CTkButton(result_frame, text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",fg_color="#4a90e2",
        hover_color="#357ABD",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(11):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="11:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [660]
                    timer_time = 660   
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)

                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",
        hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(yoga_exercises)
                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="9:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [540]     
                    is_running = [False]
                    timer_time = 540
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)

                    finish_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",
        hover_color="#357ABD",text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "30" and intensity == "EASY" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="11:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [600]     
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",
        hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(6):
                        exercise = random.choice(eqp_exercises)

                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="11:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [660]     
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame,fg_color="#4a90e2", hover_color="#357ABD", text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="9:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [540]     
                    is_running = [False]
                    timer_time = 540
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "30" and intensity == "MODERATE" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [600]     
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(10):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]     
                    is_running = [False]
                    timer_time = 900
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="9:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [540]     
                    is_running = [False]
                    timer_time = 540
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "30" and intensity == "MODERATE" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)
                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    
                    title.pack(pady=10)

                    for i in range(5):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(5):
                        exercise = random.choice(eqp_exercises)
                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]
                    timer_time = 900
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)

                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="9:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [540]     
                    is_running = [False]
                    timer_time = 540
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "30" and intensity == "HARD" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
         
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(10):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]
                    timer_time = 900
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="9:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [540]     
                    is_running = [False]
                    timer_time = 540
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "30" and intensity == "HARD" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(5):
                        exercise = random.choice(eqp_exercises)

                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]
                    timer_time = 900
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)

                    next_button =  ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="9:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [540]     
                    is_running = [False]
                    timer_time = 540
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()       
        if duration == "45" and intensity == "EASY" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
          
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(23):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="23:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1380]
                    timer_time = 1380
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(8):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="12:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [720]     
                    is_running = [False]
                    timer_time = 720
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "45" and intensity == "EASY" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            

                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")

                
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    
                    next_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)

                elif mode[0]== "cardio":
                    title2 = "CARDIO"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(13):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(10):
                        exercise = random.choice(eqp_exercises)

                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="23:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1380]
                    timer_time = 1380
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)

                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(8):
                        exercise = random.choice(yoga_exercises)
                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="12:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [720]     
                    is_running = [False]
                    timer_time = 720
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "45" and intensity == "MODERATE" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            

                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(10):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="20:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1200]
                    timer_time = 1200
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(10):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]     
                    is_running = [False]
                    timer_time = 900
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()        
        if duration == "45" and intensity == "MODERATE" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            

                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(5):
                        exercise = random.choice(eqp_exercises)

                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="20:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1200]
                    timer_time = 1200
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(10):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]     
                    is_running = [False]
                    timer_time = 900
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "45" and intensity == "HARD" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            

                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
     
                    for i in range(10):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="20:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1200]
                    timer_time = 1200
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    all_yoga=[]
                    for i in range(10):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]     
                    is_running = [False]
                    timer_time = 900
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()        
        if duration == "45" and intensity == "HARD" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            

                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)

                    for i in range(5):
                        exercise = random.choice(warmup_exercises)
                        print(exercise)
                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="10:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [600]
                    is_running = [False]
                    timer_time = 600
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
  
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(5):
                        exercise = random.choice(eqp_exercises)

                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="20:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1200]
                    timer_time = 1200
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    all_yoga=[]
                    for i in range(10):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 1.5MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="15:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [900]     
                    is_running = [False]
                    timer_time = 900
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "60" and intensity == "EASY" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)

                    for i in range(5):
                        exercise = random.choice(warmup_exercises)
                        print(exercise)
                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="20:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [1200]
                    is_running = [False]
                    timer_time = 1200
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)

                    for i in range(12):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="24:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1440]
                    timer_time = 1440
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(8):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="16:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [960]     
                    is_running = [False]
                    timer_time = 960
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "60" and intensity == "EASY" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="20:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [1200]
                    is_running = [False]
                    timer_time = 1200
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
        
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(6):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(6):
                        exercise = random.choice(eqp_exercises)

                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="24:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [1440]
                    timer_time = 1440
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(8):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="16:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [960]     
                    is_running = [False]
                    timer_time = 960
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()    
        if duration == "60" and intensity == "MODERATE" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color = "#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [480]
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
    
                    for i in range(11):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="44:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [2640]
                    timer_time = 2640
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [480]     
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame,fg_color="#4a90e2",hover_color="#357ABD", text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "60" and intensity == "MODERATE" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [480]
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="NEXT", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(5):
                        exercise = random.choice(cardio_exercises)
                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(6):
                        exercise = random.choice(eqp_exercises)
                        print(exercise)
                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="44:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [2640]
                    timer_time = 2640
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(yoga_exercises)
                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [480]     
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()        
        if duration == "60" and intensity == "HARD" and eqp == "NO": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                exercise_list = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"

                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(warmup_exercises)

                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [480]
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
       
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(11):
                        exercise = random.choice(cardio_exercises)

                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="44:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [2640]
                    timer_time = 2640
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    all_yoga=[]
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [480]     
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, text="FINISH",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work()
        if duration == "60" and intensity == "HARD" and eqp == "YES": 
            mode = ["warmup"]
            all_warmup=[]
            all_cardio=[]
            all_yoga=[]
            def work():

                warmup_exercises = [Jumping_Jacks, Arm_Swings, Hip_Circles, Leg_Swings, Torso_Twists,]
                cardio_exercises = [Lunges_with_Rotation, Skater_Steps, Inchworms, Mountain_Climbers, Burpees, Jump_Squats, Running_in_Place, Butt_Kicks, High_Knees_2, Skater_Jumps, Jump_Rope, Box_Jumps, Plank_Jacks, Push_Ups, Squats, Lunges, Plank_Shoulder_Taps, Glute_Bridges, Tricep_Dips, Bicycle_Crunches, Wall_Sit, Superman_Hold, Side_Plank]
                eqp_exercises = [Dumbbell_Squats, Resistance_Band_Rows, Kettlebell_Swings, Barbell_Bench_Press, Medicine_Ball_Slams, Cable_Chest_Fly, Leg_Press, Lat_Pulldown, Weighted_Step_Ups, Battle_Rope_Waves]
                yoga_exercises = [Downward_Dog, Cobra_Pose, Childs_Pose, Warrior_II, Cat_Cow, Bridge_Pose, Triangle_Pose, Seated_Forward_Bend, Tree_Pose, Pigeon_Pose]
            
                result_frame = ctk.CTkScrollableFrame(win,height=700,width = 1300, fg_color="#1f2a38", corner_radius=15)
                result_frame.place(relx=0.5, rely=0.5, anchor="center")
                title2 = ""
                title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 26, "bold"))
                title.pack(pady=10)
                def go_next(frame):
                    frame.destroy()  
                    if mode == ['warmup']:       
                        mode[0] = "cardio"   
                    elif mode == ["cardio"]:
                        mode[0] = 'yoga'
                    work()    
                if mode[0] == "warmup":
                    title2 = "WARMUP"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))

                    title.pack(pady=10)
                    for i in range(4):
                        exercise = random.choice(warmup_exercises)
                        all_warmup.append(exercise)
                        warmup_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 1MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)
                   
                    timer_seconds = [480]
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT",fg_color="#4a90e2",hover_color="#357ABD", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0]== "cardio":
                    title2 = "CARDIO"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    
                    for i in range(5):
                        exercise = random.choice(cardio_exercises)
                        all_cardio.append(exercise)
                        cardio_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    for i in range(6):
                        exercise = random.choice(eqp_exercises)
                        print(exercise)
                        all_cardio.append(exercise)
                        eqp_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "2SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="44:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [2640]
                    timer_time = 2640
                    is_running = [False]
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    next_button = ctk.CTkButton(result_frame, text="NEXT", fg_color="#4a90e2",hover_color="#357ABD",font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: go_next(result_frame))
                    next_button.pack(padx=100,pady=9)
                elif mode[0] == "yoga":
                    title2 = "WARM DOWN"
                    title = ctk.CTkLabel(result_frame, text=title2, font=("Arial", 32, "bold"))
                    title.pack(pady=10)
                    all_yoga=[]
                    for i in range(4):
                        exercise = random.choice(yoga_exercises)

                        all_yoga.append(exercise)
                        yoga_exercises.remove(exercise)
                        name = exercise[0]          
                        desc = exercise[1]   
                        set = "1SETS X 2MIN"     
                        ex_label = ctk.CTkLabel(result_frame,text=f"{name}\n{desc}\n{set}",font=("Arial", 16),justify="left",anchor="w")
                        ex_label.pack(fill="x", padx=15, pady=8)
                    timer_label = ctk.CTkLabel(result_frame, text="8:00", font=("Arial", 28, "bold"))
                    timer_label.pack(pady=10)

                    timer_seconds = [480]     
                    is_running = [False]
                    timer_time = 480
                    timer(timer_seconds,is_running,timer_label,result_frame,timer_time)
                    finish_button = ctk.CTkButton(result_frame, fg_color="#4a90e2",hover_color="#357ABD",text="FINISH", font=("Arial Bold", 20),width=150, height=45, text_color="white",command=lambda: [finish_and_save_pdf(all_warmup, all_cardio, all_yoga)])
                    finish_button.pack(padx=100,pady=9)
            work() 
    workout_selection()
    win.mainloop()