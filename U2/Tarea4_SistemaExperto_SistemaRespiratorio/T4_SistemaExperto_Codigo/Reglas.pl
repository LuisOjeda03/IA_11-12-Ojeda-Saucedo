% reglas.pl

evaluar :-
    writeln("Sistema Experto: Diagnostico de Enfermedades Respiratorias"),
    hipotesis(Enfermedad),
    write("El paciente posiblemente tiene: "),
    writeln(Enfermedad),
    deshacer, !.

% Hipótesis de enfermedades
hipotesis(asbestosis) :- asbestosis.
hipotesis(asma) :- asma.
hipotesis(bronquitis) :- bronquitis.
hipotesis(epoc) :- epoc.
hipotesis(resfriado_comun) :- resfriado_comun.
hipotesis(covid_19) :- covid_19.
hipotesis(crup) :- crup.
hipotesis(influenza) :- influenza.
hipotesis(neumonia) :- neumonia.
hipotesis(tos_ferina) :- tos_ferina.
hipotesis(pleuresia) :- pleuresia.
hipotesis(ipf) :- ipf.
hipotesis(hipertension_pulmonar) :- hipertension_pulmonar.
hipotesis(apnea) :- apnea.
hipotesis(cancer_pulmonar) :- cancer_pulmonar.
hipotesis(rsv) :- rsv.

hipotesis(no_identificado).

% Regla No. 1 - Asbestosis
asbestosis :-
    verificar(sentirse_sin_aliento),
    verificar(tos_seca),
    verificar(dolor_en_el_pecho).

% Regla No. 2 - Asma
asma :-
    verificar(sibilancia),
    verificar(palido),
    verificar(opresion_en_el_pecho),
    verificar(dificultad_para_hablar),
    verificar(dificultad_para_respirar),
    verificar(inconsciencia),
    verificar(falta_de_aliento),
    verificar(sudoracion), 
    verificar(tos).

% Regla No. 3 - Bronquitis
bronquitis :-
    verificar(dolor_de_garganta),
    verificar(secrecion_nasal),
    verificar(dolor_de_cabeza),
    verificar(tos),
    verificar(toser_moco),
    verificar(dificultad_para_respirar),
    verificar(dificultad_al_acostarse),
    verificar(fiebre_alta),
    verificar(dolor_en_el_pecho),
    verificar(dolor_en_el_hombro).

% Regla No. 4 - Enfermedad Pulmonar Obstructiva Cronica (EPOC)
epoc :-
    verificar(dificultad_para_respirar),
    verificar(tos_cronica),
    verificar(mucosidad_excesiva),
    verificar(sibilancia),
    verificar(dolor_en_el_pecho).
    

% Regla No. 5 - Resfriado comun
resfriado_comun :-
    verificar(dolor_de_garganta),
    verificar(tos),
    (verificar(secrecion_nasal) ; verificar(congestion_nasal)),
    verificar(sentirse_cansado),
    verificar(estornudos),
    verificar(dolor_de_cabeza),
    verificar(dolor_muscular).

% Regla No. 6 - Covid - 19
covid_19 :-
    verificar(tos),
    verificar(dolor_de_garganta),
    verificar(diarrea),
    verificar(congestion_nasal),
    verificar(dificultad_para_respirar),
    verificar(fiebre_alta),
    verificar(nauseas),
    verificar(perdida_del_gusto),
    (verificar(sentirse_cansado) ; verificar(sentirse_agotado)).

% Regla No. 7 - Crup
crup :-
    verificar(tos),
    verificar(sibilancia),
    verificar(voz_ronca),
    (verificar(secrecion_nasal) ; verificar(congestion_nasal)),
    verificar(fiebre_alta),
    verificar(sentirse_cansado).

% Regla No. 8 - Influenza o gripe
influenza :-
    verificar(dolor_de_garganta),
    verificar(dolor_muscular),
    verificar(escalofrios),
    verificar(fiebre_alta),
    (verificar(sentirse_cansado) ; verificar(sentirse_agotado)),
    verificar(ojos_llorosos),
    verificar(perdida_del_apetito),
    verificar(secrecion_nasal),
    verificar(tos).

% Regla No. 9 - Neumonia
neumonia :- 
    verificar(fiebre_alta),
    verificar(tos_con_flema),
    verificar(dificultad_para_respirar),
    verificar(fatiga_intensa),
    verificar(malestar_en_general),
    verificar(dolor_en_el_pecho).


% Regla No. 10 - Tos Ferina
tos_ferina :-
    verificar(tos),
    verificar(fiebre_alta),
    verificar(congestion_nasal),
    (verificar(congestion_nasal) ; verificar(secrecion_nasal)),
    (verificar(sentirse_cansado) ; verificar(sentirse_agotado)).

% Regla No. 11 - Pleuresia
pleuresia :-
    verificar(dolor_en_el_pecho_pulzante),
    verificar(dificultad_para_respirar),
    verificar(tos_seca),
    (verificar(sentirse_cansado) ; verificar(sentirse_agotado)),
    verificar(dolor_muscular),
    verificar(perdida_del_apetito),
    verificar(escalofrios),
    verificar(fiebre_alta),
    verificar(latidos_cardiacos_rapidos).

    
% Regla No. 12 - Fibrosis Pulmonar Idiopatica (IPF)
ipf :-
    verificar(sentirse_sin_aliento),
    verificar(dolor_en_el_pecho),
    verificar(perdida_del_apetito),
    verificar(perdida_de_peso),
    (verificar(sentirse_cansado) ; verificar(sentirse_agotado)),
    verificar(tos_cronica),
    verificar(deformacion_en_su_dedo).

% Regla No. 13- Hipertension Pulmonar HP
hipertension_pulmonar :-
    verificar(dolor_en_el_pecho),
    verificar(sibilancia),
    verificar(tos),
    verificar(voz_ronca),
    verificar(sentirse_sin_aliento),
    verificar(mareos),
    verificar(latidos_cardiacos_rapidos),
    (verificar(sentirse_cansado) ; verificar(sentirse_agotado)),
    verificar(hinchazon_en_la_parte_baja),
    verificar(labios_azules).

% Regla No. 14 - Apnea Obstructiva del Sueño
apnea :-
    verificar(ruidos_fuertes_al_dormir),
    verificar(pausas_en_la_respiracion),
    verificar(tos),
    verificar(sudoracion),
    verificar(somnolencia).

% Regla No. 15 - Cancer Pulmonar
cancer_pulmonar :-
    verificar(hinchazon_en_la_parte_baja),
    verificar(tos_cronica),
    verificar(dolor_en_el_pecho),
    verificar(tos_con_sangre),
    verificar(sentirse_sin_aliento),
    verificar(sibilancia),
    verificar(voz_ronca),
    verificar(cuello_y_cara_hinchadoz),
    verificar(perdida_del_apetito),
    verificar(dolor_de_espalda),
    verificar(dolor_de_huesos),
    verificar(dolor_de_cabeza),
    verificar(deformacion_en_su_dedo).

% Regla No. 16 - RSV Virus Senticial Respiratorio
rsv :-
    verificar(tos),
    verificar(deshidratado),
    verificar(dolor_de_garganta),
    verificar(dificultad_para_respirar),
    verificar(fiebre_alta),
    verificar(infeccion_de_oido),
    verificar(labios_azules),
    verificar(respiracion_acelerada),
    verificar(perdida_del_apetito),
    verificar(sibilancia),
    (verificar(congestion_nasal) ; verificar(secrecion_nasal)).

% Preguntar al usuario
preguntar(Pregunta) :-
    write('El paciente presenta el sintoma: '),
    write(Pregunta),
    write('? (si./no.): '),
    read(Respuesta),
    nl,
    ((Respuesta == si) -> assert(si(Pregunta)) ; assert(no(Pregunta)), fail).

% Manejo dinámico de respuestas
:- dynamic si/1, no/1.

verificar(S) :- (si(S) -> true ; (no(S) -> fail ; preguntar(S))).

% Limpieza de hechos
deshacer :- retract(si(_)), fail.
deshacer :- retract(no(_)), fail.
deshacer.