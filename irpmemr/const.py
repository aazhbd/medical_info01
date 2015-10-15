# -*- coding: utf-8 -*-

TOILET_CHOICES = (
        ('F', 'Flush'),
        ('PT', 'Pit toilet'),
        ('TPT', 'Traditional Pit toilet'),
        ('L', 'Latrine'),
        ('BF', 'Bush /Field'),
        ('R', 'River'),
	('O', 'Others'),
)

COOKING_FACILITIES = (
        ('Electricity', 'Electricity'),
        ('Gas', 'Gas'),
        ('Biomass', 'Biomass'),
        ('Kerosene', 'Kerosene'),
        ('Coal', 'Coal'),
        ('Charcoal', 'Charcoal'),
	('Firewood', 'Firewood'),
	('Others', 'Others'),
)

SEX_CHOICES = (
    ("M","Male"),
    ("F","Female"),
    ("O","Others"),
)

MARITAL_CHOICES = (
    ('SG', 'Single'),
    ('MR', 'Married'),
    ('DV', 'Divorced'),
    ('WD', 'Widowed'),
)

FREQUENCY_CHOICES = (
    ('AL', 'Always'),
    ('US', 'Usually'),
    ('OF', 'Often'),
    ('SO', 'Sometimes'),
    ('SE', 'Seldom'),
    ('RA', 'Rarely'),
    ('NV', 'Never'),
)

LITERATE_CHOICES = (
    ('LT', 'Literate'),
    ('SL', 'Semiliterate'),
    ('IL', 'Iliterate'),
)

LEVEL_CHOICES = (
    ('No', 'No'),
    ('Mi', 'Mild'),
    ('Mo', 'Moderate'),
    ('S', 'Severe'),
)

EDUCATIONAL_LEVEL_CHOICES = (
    ('KD', 'Kindergarden'),
    ('PR', 'Primary'),
    ('SC', 'Secondary'),
    ('UN', 'University'),
    ('NV', 'Never'),
)

RELATIONSHIP_CHOICES = (
    ('HS', 'Husband'),
    ('FA', 'Father'),
    ('MO', 'Mother'),
    ('GF', 'Grandfather'),
    ('GM', 'Grandmother'),
    ('UN', 'Uncle'),
    ('AU', 'Aunt'),
    ('FR', 'Friend'),
)

MENSTRUAL_CYCLE_CHOICES = (
    ('28', '28days'),
    ('30', '30days'),
    ('OT', 'Others'),
)

HAVE_BEEN_PREGNANT_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),
    (20, '20'),
)

TYPES_OF_DELIVERY_CHOICES = (
    ('LB', 'Live Birth'),
    ('SB', 'Still Birth'),
    ('AB', 'Abortion'),
    ('EC', 'Ectopic'),
    ('HM', 'Hydatidiform Model'),
    ('OT', 'Others'),
)

PROBLEMS_CHOICES = (
    ('NO', 'None'),
    ('PL','PretermLabor'),
    ('DB','Diabetes'),
    ('HB','High Blood Pressure'),
    ('TH','Thrombosis'),
    ('EM','Embolus'),
    ('HT','Hypertension'),
    ('PE','Pre-Eclampsia'),
    ('EC','Eclampsia'),
    ('OT','Others'),
)

OBSTETRICALOPERATION_CHOICES = (
    ('NO', 'None'),
    ('CS', 'Caesarian Section'),
    ('FO','Forceps'),
    ('VE','Vacuum Extraction'),
    ('MI','Manual instrumental help in vaginal breech delivery'),
    ('MR','Manual Removal Of The Placenta'),
    ('OT','Others'),
)

METHOD_OF_BIRTH_CONTROL_CHOICES = (
    ('CO', 'Condoms'),
    ('PI', 'Pills'),
    ('PA', 'Patch'),
    ('VR', 'Vaginal Ring'),
    ('TU', 'Tubal/Essure'),
    ('IU', 'IUD'),
    ('PV', 'Partner with vasectomy'),
    ('NA', 'Natural Family Planning'),
    ('IM', 'Implanon'),
    ('NO', 'None'),
    ('OT', 'Other'),
)

NORMAL_CHOICES = (
    ('NR', 'Normal'),
    ('AB', 'Abnormal'),
)

VACCINATION_CHOICES= (
    ('RU', 'Rubella'),
    ('TT', 'Tetanus Toxoid'),
    ('OT', 'Other'),
)

VISIT_CHOICES = (
    ('FT', 'First trimester'),
    ('ST', 'Second Trimester'),
    ('TT', 'Third Trimester'),
    ('OT', 'Other visit'),
)

BLOOD_PRESSURE_CHOICES = (
    ('BE','140/90'),
    ('AB','>= 140/90'),
)

URINALYSIS_CHOICES = (
    ('BE', '<0.3g/24h'),
    ('AB', '>0.3g/24h'),
)

HEMOGLOBIN_CHOICES = (
    ('A', '9-10'),
    ('B', '7-8'),
    ('C', '<7'),
    ('D', '>=11'),
)

MATERNAL_COMPLICATIONS_CHOICES = (
    ('NO','No complication'),
    ('RA', 'Recurrent early abortion'),
    ('IA','Induced abortion and any associated complications'),
    ('TH','Thrombosis'),
    ('EM','Embolus'),
    ('HY','Hypertension'),
    ('PE','Pre-Eclampsia'),
    ('EC','Eclampsia'),
    ('PA','Placental abruption'),
    ('OT','Others'),
)

PERINATAL_COMPLICATIONS_CHOICES = (
    ('NO','No complication'),
    ('TW', 'Twins or higher order multiples'),
    ('LO', 'Low birth weight (<2500g)'),
    ('IG','Intrauterine growth retardation'),
    ('RA','Rhesus antibody(erytroblastosis,hydrops)'),
    ('MC','Malformed or chromosomally abnormal child'),
    ('MA','macrosomic(>4500g) newborn'),
    ('RE','Resuscitation or other treatment of newborn'),
    ('PE','Perinatal,neonatal or infant death'),
    ('OT','Others'),
)
