from adappmailles.modele.motif import Motif
from adappmailles.modele.rang_instructions import RangInstructions
from adappmailles.modele.rang import TypeRang


def get_motifs_test_listes():
    def K(n=1):
        return [("K", n)]

    def P(n=1):
        return [("P", n)]

    r1_jersey = RangInstructions(
        avant=[],
        repetees=K(1),
        apres=[]
    )
    r2_jersey = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(1),
        apres=[]
    )

    jersey = Motif(
        nom_motif="Jersey",
        instructions=[r1_jersey, r2_jersey],
        coefficient=1,
        couleur_motif="ivory"
    )

    r1_mousse = RangInstructions(
        avant=[],
        repetees=K(1),
        apres=[]
    )
    r2_mousse = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1),
        apres=[]
    )

    mousse = Motif(
        nom_motif="Mousse",
        instructions=[r1_mousse, r2_mousse],
        coefficient=1,
        couleur_motif="light blue"
    )

    r1_moss_stitch = RangInstructions (
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(2) + P(2),
        apres=[]
    )
    r2_moss_stitch = RangInstructions(
        type_rang = TypeRang.ENVERS,
        avant=[],
        repetees=P(2) + K(2),
        apres = []
    )
    r3_moss_stitch = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees = P(2) + K(2),
        apres=[]
    )
    r4_moss_stitch = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees = K(2) + P(2),
        apres=[]
    )
    moss_stitch = Motif(
        nom_motif="Moss Stitch",
        instructions=[r1_moss_stitch, r2_moss_stitch, r3_moss_stitch, r4_moss_stitch],
        coefficient=1,
        couleur_motif="plum"
    )

    r1_seed_blocks = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(1) + K(1) + P(1) + K(3),
        apres=K(1)+P(1)+K(1)+P(1)+K(1)
    )

    r2_seed_blocks = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=(K(1) + P(1)) * 2 + K(1),
        repetees=P(2) + (K(1) + P(1)) * 2 + K(1),
        apres=[]
    )

    r3_seed_blocks = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(1) + K(1) + P(1) + K(3),
        apres=K(1)+P(1)+K(1)+P(1)+K(1)
    )

    r4_seed_blocks = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=(K(1) + P(1)) * 2 + K(1),
        repetees=P(2) + (K(1) + P(1)) * 2 + K(1),
        apres=[]
    )

    r5_seed_blocks = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(1) + K(1) + P(1) + K(3),
        apres=K(1)+P(1)+K(1)+P(1)+K(1)
    )

    r6_seed_blocks = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=(K(1) + P(1)) * 2 + K(1),
        repetees=P(2) + (K(1) + P(1)) * 2 + K(1),
        apres=[]
    )

    r7_seed_blocks = RangInstructions(
        avant=[],
        repetees = P(12),
        apres=[]
    )

    r8_seed_blocks = RangInstructions(
        avant=[],
        repetees=K(12),
        apres=[]
    )

    seed_blocks = Motif(
        nom_motif="Seed Blocks",
        instructions=[r1_seed_blocks, r2_seed_blocks, r3_seed_blocks, r4_seed_blocks, r5_seed_blocks, r6_seed_blocks, r7_seed_blocks, r8_seed_blocks],
        coefficient=1,
        couleur_motif="red"
    )

    r1_seed_stitch =  RangInstructions(
        avant = K(1),
        repetees = P(1)  + K(1),
        apres = []
    )
    r2_seed_stitch = RangInstructions(
        type_rang = TypeRang.ENVERS,
        avant = K(1),
        repetees = P(1) + K(1),
        apres = []
    )
    seed_stitch = Motif(
        nom_motif="Seed Stitch",
        instructions = [r1_seed_stitch, r2_seed_stitch],
        coefficient=1,
        couleur_motif="pale green"
    )

    r1_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(7)+K(2)+P(7),
        apres=[]
    )

    r2_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(6)+P(4)+K(6),
        apres=[]
    )

    r3_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(5)+K(2)+P(2)+K(2)+P(5),
        apres=[]
    )

    r4_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(4) +(P(2)+K(1))*2 + P(2) + K(4),
        apres=[]
    )

    r5_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(3) + (K(2)+ P(2)) * 2 + K(2) + P(3),
        apres=[]
    )

    r6_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=(K(2) + P(2) + K(1) + P(2)) * 2 + K(2),
        apres=[]
    )        

    r7_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(P(2) + K(2)+ P(1) + K(2)) * 2 + P(2),
        apres=[]
    )

    r8_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(3) + (P(2) + K(2)) * 2 + P(2) + K(3),
        apres=[]
    )

    r9_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(4) + (K(2) + P(1)) *2 + K(2) + P(4),
        apres=[]
    )

    r10_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(5) + P(2) + K(2) + P(2) + K(5),
        apres=[]
    )

    r11_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(6) + K(4) + P(6),
        apres=[]
    )

    r12_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(7) + P(2) + K(7),
        apres=[]
    )

    r13_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(14) + K(1),
        apres=[]
    )

    r14_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(2) + K(12) + P(2),
        apres=[]
    )

    r15_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(1) + K(2) + P(10) + K(2) + P(1),
        apres=[]
    )

    r16_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(1) + K(1) + P(2) + K(8) + P(2) + K(1) + P(1),
        apres=[]
    )

    r17_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(2) + K(2) + P(6) + K(2) + P(2) + K(1),
        apres=[]
    )

    r18_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=(K(1) + P(2)) * 2 + K(4) + (P(2) + K(1)) *2,
        apres=[]
    )

    r19_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(P(1) + K(2)) * 2 + P(4) +(K(2) + P(1)) * 2,
        apres=[]
    )

    r20_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(1) + K(2) + P(2) + K(6) + P(2) + K(2) + P(1),
        apres=[]
    )

    r21_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(1) + K(2) + P(8) + K(2) + P(1) + K(1),
        apres=[]
    )

    r22_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(2) + K(10) + P(2) + K(1),
        apres=[]
    )

    r23_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(2) + P(12) + K(2),
        apres=[]
    )

    r24_moss_diamonds = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(1) + K(14) + P(1),
        apres=[]
    )

    moss_diamonds = Motif(
        nom_motif="Moss Diamonds",
        instructions = [r1_moss_diamonds, r2_moss_diamonds, r3_moss_diamonds, r4_moss_diamonds,
                  r5_moss_diamonds, r6_moss_diamonds, r7_moss_diamonds, r8_moss_diamonds,
                  r9_moss_diamonds, r10_moss_diamonds, r11_moss_diamonds, r12_moss_diamonds,
                  r13_moss_diamonds, r14_moss_diamonds, r15_moss_diamonds, r16_moss_diamonds,
                  r17_moss_diamonds, r18_moss_diamonds, r19_moss_diamonds, r20_moss_diamonds,
                  r21_moss_diamonds, r22_moss_diamonds, r23_moss_diamonds, r24_moss_diamonds],
        coefficient=1,
        couleur_motif="green"
    )

    r1_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= K(6) + P(1) + K(5),
        apres=K(1)
    )

    r2_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=P(1),
        repetees=P(4) + K(1) + P(1) + K(1) + P(5),
        apres=[]
    )

    r3_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= K(4) + (P(1) + K(3))*2,
        apres=K(1)
    )

    r4_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=P(1),
        repetees=P(2) + K(1) + P(5) + K(1) + P(3),
        apres=[]
    )

    r5_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= K(2) + P(1) + K(7) + P(1) + K(1),
        apres=K(1)
    )

    r6_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=P(1),
        repetees=K(1) + P(9) + K(1) + P(1),
        apres=[]
    )

    r7_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= P(1) + K(11),
        apres=P(1)
    )

    r8_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=P(1),
        repetees=K(1) + P(9) + K(1) + P(1),
        apres=[]
    )

    r9_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= K(2) + P(1) + K(7) + P(1) + K(1),
        apres=K(1)
    )

    r10_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=P(1),
        repetees=P(2) + K(1) + P(5) + K(1) + P(3),
        apres=[]
    )

    r11_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= K(4) + (P(1) + K(3))*2,
        apres=K(1)
    )

    r12_seeded_windowpane = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=P(1),
        repetees=P(4) + K(1) + P(1) + K(1) + P(5),
        apres=[]
    )

    seeded_windowpane = Motif(
        nom_motif="Seeded Windowpane",
        instructions=[r1_seeded_windowpane, r2_seeded_windowpane, r3_seeded_windowpane, r4_seeded_windowpane,
                r5_seeded_windowpane, r6_seeded_windowpane, r7_seeded_windowpane, r8_seeded_windowpane,
                r9_seeded_windowpane, r10_seeded_windowpane, r11_seeded_windowpane, r12_seeded_windowpane],
        coefficient=1,
        couleur_motif="yellow"
    )

    r1_single_basketweave = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=(K(1) + P(1))*3,
        apres=[]
    )

    r2_single_basketweave = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(3) + P(1),
        apres=K(2)
    )

    r3_single_basketweave = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=P(2),
        repetees=K(1) + P(3),
        apres=[]
    )

    r4_single_basketweave = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(K(1) + P(1))*3,
        apres=[]
    )

    r5_single_basketweave = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(3),
        apres=K(1) + P(1)
    )

    r6_single_basketweave = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant= K(1) + P(1),
        repetees=K(3) + P(1),
        apres=[]
    )

    single_basketweave = Motif(
        nom_motif="Single Basketweave",
        instructions=[r1_single_basketweave, r2_single_basketweave, r3_single_basketweave,
                r4_single_basketweave, r5_single_basketweave, r6_single_basketweave],
        coefficient=1,
        couleur_motif="brown"
    )


    r1_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant = [],
        repetees=K(1) + P(1) + K(1) + P(5),
        apres=[]
    )
    r2_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees = K(5) + P(1) + K(1) + P(1),
        apres=[]
    )
    r3_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(1) + K(5) + P(1),
        apres=[]
    )
    r4_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(5) + K(1) + P(1),
        apres=[]
    )
    r5_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(1) + P(5)+ K(1) + P(1),
        apres=[]
    )
    r6_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(1) + K(5) + P(1),
        apres=[]
    )
    r7_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees = K(5)+ P(1) +K(1) + P(1),
        apres=[]
    )
    r8_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(1) + K(1) + P(5),
        apres=[]
    )
    r9_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(4) + K(1) + P(1) + K(1) + P(1),
        apres=[]
    )
    r10_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(1) + K(1) + P(1) + K(4),
        apres=[]
    )
    r11_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(3) + P(1) + K(1) + P(1) + K(2),
        apres=[]
    )
    r12_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(2) + K(1) + P(1) + K(1) + P(3),
        apres=[]
    )
    r13_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(2) + K(1) + P(1) + K(1) + P(3),
        apres=[]
    )
    r14_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(3) + P(1) + K(1) + P(1) + K(2),
        apres=[]
    )
    r15_tv_static = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees = K(1) + P(1) + K(1) + P(1) + K(4),
        apres=[]
    )
    r16_tv_static = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(4) + K(1) + P(1) + K(1) + P(1),
        apres=[]
    )
    tv_static = Motif(
        nom_motif="TV Static",
        instructions=[r1_tv_static, r2_tv_static, r3_tv_static, r4_tv_static, r5_tv_static, r6_tv_static, r7_tv_static,r8_tv_static, r9_tv_static, r10_tv_static, r11_tv_static, r12_tv_static, r13_tv_static, r14_tv_static, r15_tv_static, r16_tv_static],
        coefficient=1,
        couleur_motif="grey"
    )

    r1_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=P(1),
        repetees=(K(2) + P(2)) * 2 + K(1) + (P(2) + K(2))*2 + P(1),
        apres=[]
    )

    r2_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + (P(2) + K(2)) * 2 + P(1) + (K(2) + P(2)) *2,
        apres= K(1)
    )

    r3_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=P(1),
        repetees=(K(2) + P(2)) * 2 + K(1) + (P(2) + K(2))*2 + P(1),
        apres=[]
    )

    r4_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + (P(2) + K(2)) * 2 + P(1) + (K(2) + P(2)) *2,
        apres= K(1)
    )

    r5_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=P(1),
        repetees=P(1) + K(2) + P(2) + K(2) + P(3) + (K(2) + P(2)) * 2,
        apres=[]
    )

    r6_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(K(2) + P(2)) * 2 + K(3) + P(2) + K(2) + P(2) + K(1),
        apres= K(1)
    )

    r7_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=P(1),
        repetees=P(1) + K(2) + P(2) + K(2) + P(3) + (K(2) + P(2)) * 2,
        apres=[]
    )

    r8_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(K(2) + P(2)) * 2 + K(3) + P(2) + K(2) + P(2) + K(1),
        apres= K(1)
    )

    r9_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=K(1),
        repetees=(P(2) + K(2)) * 2 + P(1) + (K(2) + P(2))*2 + K(1),
        apres=[]
    )

    r10_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(1) + (K(2) + P(2)) * 2 + K(1) + (P(2) + K(2)) *2,
        apres= P(1)
    ) 

    r11_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=K(1),
        repetees=(P(2) + K(2)) * 2 + P(1) + (K(2) + P(2))*2 + K(1),
        apres=[]
    )

    r12_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(1) + (K(2) + P(2)) * 2 + K(1) + (P(2) + K(2)) *2,
        apres= P(1)
    )

    r13_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=K(1),
        repetees=K(1) + P(2) + K(2) + P(2) + K(3) + (P(2) + K(2)) * 2,
        apres=[]
    )

    r14_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(P(2) + K(2)) * 2 + P(3) + K(2) + P(2) + K(2) + P(1),
        apres= P(1)
    )

    r15_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=K(1),
        repetees=K(1) + P(2) + K(2) + P(2) + K(3) + (P(2) + K(2)) * 2,
        apres=[]
    )

    r16_chevron_rib = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=(P(2) + K(2)) * 2 + P(3) + K(2) + P(2) + K(2) + P(1),
        apres= P(1)
    )

    chevron_rib = Motif(
        nom_motif="Chevron Rib",
        instructions=[r1_chevron_rib, r2_chevron_rib, r3_chevron_rib, r4_chevron_rib,
                r5_chevron_rib, r6_chevron_rib, r7_chevron_rib, r8_chevron_rib,
                r9_chevron_rib, r10_chevron_rib, r11_chevron_rib, r12_chevron_rib,
                r13_chevron_rib, r14_chevron_rib, r15_chevron_rib, r16_chevron_rib],
        coefficient=1,
        couleur_motif="blue"
    )

    r1_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(2) + (P(7) + K(1))*2,
        apres=[]
    )

    r2_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(7) + P(3) + K(7) + P(1),
        apres=[]
    )

    r3_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(7) + K(5) + P(5) + K(1),
        apres=[]
    )

    r4_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(1) + P(1) + K(3) + P(7) + K(6),
        apres=[]
    )

    r5_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(5) +K(9) +P(1) + K(1) + P(2),
        apres=[]
    )

    r6_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(3) +P(11) + K(4),
        apres=[]
    )

    r7_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(3) + K(1) + P(1) + K(9) + P(4),
        apres=[]
    )

    r8_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(5) + P(7) + K(3) +P(1) + K(2),
        apres=[]
    )

    r9_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=P(1) + K(1) + P(5) + K(5) + P(6),
        apres=[]
    )

    r10_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=K(7) + P(3) + K(7) + P(1),
        apres=[]
    )   

    r11_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees= K(2) + (P(7) + K(1)) * 2,
        apres=[]
    )

    r12_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees= P(2) + K(5) + P(1) + K(7) + P(3),
        apres=[]
    )

    r13_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(4) + P(7) + K(1) + P(3) + K(3),
        apres=[]
    )

    r14_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(4) + K(1) + P(1) + K(7) + P(5),
        apres=[]
    )

    r15_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(6) + P(7) + K(5),
        apres=[]
    )

    r16_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=P(4) + K(7) + P(1) + K(1) + P(5),
        apres=[]
    )

    r17_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=K(4) + P(3) + K(1) + P(7) + K(3),
        apres=[]
    )

    r18_crossing_paths = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees= P(2) + K(7) + P(1) + K(5) + P(3),
        apres=[]
    ) 

    crossing_paths = Motif(
        nom_motif="Crossing Paths",
        instructions=[r1_crossing_paths, r2_crossing_paths, r3_crossing_paths, r4_crossing_paths,
                r5_crossing_paths, r6_crossing_paths, r7_crossing_paths, r8_crossing_paths,
                r9_crossing_paths, r10_crossing_paths, r11_crossing_paths, r12_crossing_paths,
                r13_crossing_paths, r14_crossing_paths, r15_crossing_paths, r16_crossing_paths,
                r17_crossing_paths, r18_crossing_paths],
        coefficient=1,
        couleur_motif="pink"
    )

    return[jersey, mousse, seed_stitch, moss_stitch,
           seed_blocks,moss_diamonds, seeded_windowpane,
           single_basketweave, tv_static, chevron_rib, crossing_paths]