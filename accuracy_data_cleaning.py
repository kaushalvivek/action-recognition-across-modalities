'''
  Save accuracy for each participant accross both skeletons and avatars
'''
import json
import pandas as pd


def age_group(s):
  if s[:2] == '22':
    return 'middle_school'
  elif s[:2] == '24':
    return 'high_school'
  else:
    return 'college'


# Read file
with open("./clean_data.json") as json_file:
  data = (json.loads(json_file.read()))

bad_data = ['10_2_plane_plane.bvh', '3_3_Chicken_Quack,Goose,Wing,Chicken.bvh', '29_10_Shooting_Shooting.bvh', '27_2_Shooting_Shooting.bvh', '7_4_jurassic_jurrasic.bvh', '18_1_Mama_Woman,PregnantLady,Mother.bvh', '3_2_Horse_Horse.bvh', '19_3_Horses_Horse.bvh', '32_1_cocktail_drinkingfluidwithyourtail.bvh', '29_8_Sky_Space,Universe,Galaxy,Stars,Sky.bvh', '24_12_fillingthecarwithgas_pumpinggas,fillingthecarwithgas.bvh', '29_11_PacMan_Pac-Man.bvh', '14_4_Man_Me,Man,Suit.bvh', '1_3_crazy_crazy.bvh', '8_1_love_love.bvh', '18_1_Said_Grab,Chitchat.bvh', '29_1_Wind_Wind,Storm,Breeze.bvh', '18_2_Naked_Change,Wardrobe,Clothes,Strip,Reveal,Naked.bvh', '28_14_Decay_Dying,Rotting,Rot,Decay.bvh', '16_1_Bride_WeddingRing.bvh', '4_2_Claw_Knuckle,Hand.bvh', '28_1_Eye_Eye,Telescope.bvh', '24_5_shoppingmall_shoppingmall.bvh', '28_8_Golf_Golf.bvh', '14_1_Cheerleader_Cheerleading,Cheerleader.bvh', '27_6_Fox_Mouse,Rabbit.bvh', '24_16_practicingkarate_karatechop,kick.bvh', '27_18_Tree_Tree.bvh', '28_17_Fifa_Fifa.bvh', '20_2_Runnings_Fast,Run.bvh', '15_2_Running_Running.bvh', '27_14_Head_Head.bvh', '28_1_Mask_Mask.bvh', '29_9_Mask_Face,Mask.bvh', '27_9_Recon_Recon.bvh', '29_5_Leg_Leg.bvh', '29_6_Cry_Cry.bvh', '36_4_cry_cry.bvh', '4_1_I_I.bvh', '6_1_I_I.bvh', '8_1_I_me,I.bvh', '14_2_Electric_Shocking,Shock,Electric.bvh', '28_9_Remains_Grave.bvh', '2_4_Heaven_Angels,Heaven.bvh', '24_10_paddlingaboat_canoe,paddle.bvh', '16_3_Hat_Hat.bvh', '9_1_twist_dance,shake,boogie,twist.bvh', '4_3_Twister_Twister.bvh', '32_1_snorkeling_snorkeling.bvh', '28_12_Braid_Braid.bvh', '3_1_Walrus_SnaggleTooth,Walrus.bvh', '27_5_Bullet_Bullet.bvh', '5_3_Baby_Baby.bvh', '36_1_baby_baby.bvh', '10_1_hangover_headache,hangover.bvh', '32_1_baseball_baseball.bvh', '27_3_Cars_Drive,Cars.bvh', '8_1_rock&roll_rock&roll.bvh', '3_4_Time_Time.bvh', '13_1_Single_One,Single.bvh', '27_7_Batman_Batman.bvh', '28_13_Daddy_Daddy.bvh', '36_4_dove_pray.bvh', '8_3_dances_danceswithwolves.bvh', '15_1_Dancing_Dance.bvh', '10_5_dancing_.bvh', '27_18_See_Eyes,See.bvh', '12_3_mermaid_slinky,sexy.bvh', '13_2_Fast_Wheel.bvh', '27_18_Scary_Scary.bvh', '28_9_What_What.bvh', '15_5_Shark_Shark.bvh', '8_4_magic_magician,magic.bvh', '23_1_walking_walking.bvh', '29_10_House_House,Home.bvh', '24_9_dolphins_dolphins.bvh', '4_1_Skating_Skating.bvh', '29_7_Skater_Skating,Skater.bvh', '28_13_Dream_Sleep,Dream.bvh', '28_16_Scarf_Scarf.bvh', '4_4_Tiny_Short,Tiny.bvh', '28_3_Dog_Dog.bvh', '24_2_tent_boner,tent.bvh', '22_3_Black_Arm,Sleeve,jackeet,Leather.bvh', '7_2_ring_wrappedaroundthefinger,ring.bvh', '7_3_it_it.bvh', '11_1_kiss_kiss.bvh', '27_15_Halo_Halo.bvh', '20_1_Egyptian_Egypt,Egyptian.bvh', '22_1_In_In,Inside.bvh', '32_1_sunscreen_sunscreen.bvh', '28_6_Horizon_Horizon.bvh', '19_2_Private_Salute.bvh', '22_3_Swan_Swan.bvh', '10_4_face_face.bvh', '28_19_Space_Rising,Space.bvh', '4_4_Dancer_Dancer.bvh', '19_2_Dancer_Dancing.bvh', '15_2_Devil_Devil.bvh', '17_1_Ball_Basketball,Ball.bvh', '3_4_Book.bvh', '27_8_Within_Box,Within.bvh', '18_1_Knock_Punch,Smack.bvh', '28_19_Dead_Die,Death,Kill,Dead.bvh', '23_1_dead_dead.bvh', '28_1_Death_Decapitated,Dead,Death.bvh', '36_2_ninja_fighting,ninja.bvh', '1_3_train_train.bvh', '29_4_Sonic_Running,Sonic.bvh', '32_1_jetski_motorcycle.bvh', '10_4_scar_scar.bvh', '27_11_Down_Down.bvh', '28_9_Finch_Fly,Fairy.bvh', '29_10_Evil_Dinosaur,Evil.bvh', '27_8_Evil_Evil.bvh', '23_2_Raining_Raininig.bvh', '5_2_Singer_Sing,Singer.bvh', '27_1_Fighting_Fighting.bvh', '22_4_Fight_Fight.bvh', '28_18_Fighter_Fighter.bvh', '23_4_Cards_Cards.bvh', '27_19_Gravity_Drop,Fall,Ground,Gravity.bvh', '27_16_Lego_Lego.bvh', '28_2_Sniper_Sniper.bvh', '28_7_Nightmare_Sleep,Nightmare.bvh', '2_4_Stairway_Stairway.bvh', '18_2_Gun_Gun.bvh', '9_4_Kungfupanda_panda.bvh', '10_2_snakes_snake.bvh', '16_3_Cat_Horse,Cat,Goat.bvh', '27_5_Storm_Lightning,Storm.bvh', '27_12_Storm_Storm.bvh', '7_1_born_push.bvh', '27_17_Out_Open,In,Out.bvh', '27_6_Gliding_Spinning,Gliding.bvh', '14_4_Ant_Ant.bvh', '32_1_swimming_swimming.bvh', '24_9_swimming_swimming_.bvh', '27_9_Ghost_Ghost.bvh', '5_4_Ghost_Curved.bvh', '1_2_silence_silence.bvh', '9_3_beauty_beauty.bvh', '15_4_Pigs_Mice,Pigs.bvh', '5_3_Driver_Driver.bvh', '27_1_Driving_Driving.bvh', '5_2_Wedding_Ring,Wedding.bvh', '11_1_rose_scrub.bvh', '29_3_Star_Stars.bvh', '27_6_Stars_Stars.bvh', '12_3_little_little.bvh', '32_1_drinking_drinking.bvh', '27_17_Murder_Murder.bvh', '19_1_Murder_Murder,Murderer.bvh', '5_1_Saw_Saw.bvh', '28_11_Eve_Eve.bvh', '17_1_Wrecking_Smash,Smashing.bvh', '36_1_back_back.bvh', '20_2_Cool_Cold.bvh', '28_5_South_South.bvh', '27_4_Blood_Blood.bvh', '28_10_Farming_Farming.bvh', '2_3_Puff_Puff.bvh', '27_1_Mad_Dizzy,Crazy,Mental,Mad.bvh', '27_3_Project_Singing,Talk,Voice.bvh', '8_2_genie_spinningarecord,child.bvh', '29_4_Hedgehog_Mouse,Dragon,Dinosaur.bvh', '28_4_Ark_Arc.bvh', '15_1_Queen_Queen.bvh', '10_5_queen_.bvh', '8_2_bottle_drinking,wine.bvh', '22_1_Bottle_Drink.bvh', '28_15_Far_Point,Far.bvh']

user_date = []
skeleton_accuracy = []
total_skeletons = []
avatar_accuracy = []
total_avatars = []

for i in data:
  user_date.append(i[0])
  correct_skeleton = 0
  total_skeleton = 0
  correct_avatar = 0
  total_avatar = 0

  for j in i[1]:
    if j['file'] not in bad_data:
      if j['cans'] == j['guess']:
        if j['file'].find('.fbx') == -1:
          correct_skeleton +=1
        else:
          correct_avatar +=1

      if j['file'].find('.bvh') == -1:
        total_avatar +=1
      else:
        total_skeleton +=1
  
  skeleton_accuracy.append(round((correct_skeleton/total_skeleton)*100,2))
  avatar_accuracy.append(round((correct_avatar/total_avatar)*100,2))
  total_skeletons.append(total_skeleton)
  total_avatars.append(total_avatar)

dataset = pd.DataFrame({
  'user_age_group':user_date,
  'skeleton_accuracy':skeleton_accuracy,
  'total_skeleton':total_skeletons,
  'avatar_accuracy':avatar_accuracy,
  'total_avatar':total_avatars,
})

# assign age group to the user of each datapoint
dataset['user_age_group'] = dataset['user_age_group'].map(age_group)

dataset.to_csv('accuracy_data.csv')