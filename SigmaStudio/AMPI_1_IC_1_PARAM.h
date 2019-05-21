/*
 * File:           C:\Users\Stefan\PycharmProjects\AMPI\SigmaStudio\AMPI_1_IC_1_PARAM.h
 *
 * Created:        Thursday, May 23, 2019 7:06:18 PM
 * Description:    AMPI_1:IC 1 parameter RAM definitions.
 *
 * This software is distributed in the hope that it will be useful,
 * but is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *
 * This software may only be used to program products purchased from
 * Analog Devices for incorporation by you into audio products that
 * are intended for resale to audio product end users. This software
 * may not be distributed whole or in any part to third parties.
 *
 * Copyright ©2019 Analog Devices, Inc. All rights reserved.
 */
#ifndef __AMPI_1_IC_1_PARAM_H__
#define __AMPI_1_IC_1_PARAM_H__


/* Module Mix_Aux_Mic_OUT - Stereo Switch Nx2*/
#define COUNT_MIX_AUX_MIC_OUT                          1
#define DEVICE_MIX_AUX_MIC_OUT                         "IC1"
#define ADDR_MIX_AUX_MIC_OUT_STEREOSWSLEW              0
#define FIXPT_MIX_AUX_MIC_OUT_STEREOSWSLEW             0x00000000
#define VALUE_MIX_AUX_MIC_OUT_STEREOSWSLEW             SIGMASTUDIOTYPE_INTEGER_CONVERT(0)
#define TYPE_MIX_AUX_MIC_OUT_STEREOSWSLEW              SIGMASTUDIOTYPE_INTEGER

/* Module Mix_Aux_Mic_IN - Stereo Switch Nx2*/
#define COUNT_MIX_AUX_MIC_IN                           1
#define DEVICE_MIX_AUX_MIC_IN                          "IC1"
#define ADDR_MIX_AUX_MIC_IN_STEREOSWSLEW               1
#define FIXPT_MIX_AUX_MIC_IN_STEREOSWSLEW              0x00000001
#define VALUE_MIX_AUX_MIC_IN_STEREOSWSLEW              SIGMASTUDIOTYPE_INTEGER_CONVERT(1)
#define TYPE_MIX_AUX_MIC_IN_STEREOSWSLEW               SIGMASTUDIOTYPE_INTEGER

/* Module SW vol 1 - Single slew ext vol*/
#define COUNT_SWVOL1                                   1
#define DEVICE_SWVOL1                                  "IC1"
#define ADDR_SWVOL1_STEP                               2
#define FIXPT_SWVOL1_STEP                              0x00000800
#define VALUE_SWVOL1_STEP                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000244140625)
#define TYPE_SWVOL1_STEP                               SIGMASTUDIOTYPE_FIXPOINT

/* Module Multiple 1 - Multiple Volume Control*/
#define COUNT_MULTIPLE1                                2
#define DEVICE_MULTIPLE1                               "IC1"
#define ADDR_MULTIPLE1                                 3
#define FIXPT_MULTIPLE1                                0x01FD93C1
#define VALUE_MULTIPLE1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(3.98107170553497)
#define TYPE_MULTIPLE1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_MULTIPLE1_1                               4
#define FIXPT_MULTIPLE1_1                              0x0194C583
#define VALUE_MULTIPLE1_1                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(3.16227766016838)
#define TYPE_MULTIPLE1_1                               SIGMASTUDIOTYPE_FIXPOINT

/* Module Gen Filter1_2 - General (2nd order)*/
#define COUNT_GENFILTER1_2                             5
#define DEVICE_GENFILTER1_2                            "IC1"
#define ADDR_GENFILTER1_2_ST0_B0                       5
#define FIXPT_GENFILTER1_2_ST0_B0                      0x00058026
#define VALUE_GENFILTER1_2_ST0_B0                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.042973364483739)
#define TYPE_GENFILTER1_2_ST0_B0                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_B1                       6
#define FIXPT_GENFILTER1_2_ST0_B1                      0x00000000
#define VALUE_GENFILTER1_2_ST0_B1                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_GENFILTER1_2_ST0_B1                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_B2                       7
#define FIXPT_GENFILTER1_2_ST0_B2                      0xFFFA7FDA
#define VALUE_GENFILTER1_2_ST0_B2                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.042973364483739)
#define TYPE_GENFILTER1_2_ST0_B2                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_A1                       8
#define FIXPT_GENFILTER1_2_ST0_A1                      0x00F47968
#define VALUE_GENFILTER1_2_ST0_A1                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.90995513605384)
#define TYPE_GENFILTER1_2_ST0_A1                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_A2                       9
#define FIXPT_GENFILTER1_2_ST0_A2                      0xFF8B004E
#define VALUE_GENFILTER1_2_ST0_A2                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.914053271032522)
#define TYPE_GENFILTER1_2_ST0_A2                       SIGMASTUDIOTYPE_FIXPOINT

/* Module Loudness L&H1 - Loudness (Low & Hi)*/
#define COUNT_LOUDNESSLH1                              8
#define DEVICE_LOUDNESSLH1                             "IC1"
#define ADDR_LOUDNESSLH1_LEVEL0                        10
#define FIXPT_LOUDNESSLH1_LEVEL0                       0x01028F5C
#define VALUE_LOUDNESSLH1_LEVEL0                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(2.02)
#define TYPE_LOUDNESSLH1_LEVEL0                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_LEVEL1                        11
#define FIXPT_LOUDNESSLH1_LEVEL1                       0x00D47AE1
#define VALUE_LOUDNESSLH1_LEVEL1                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.66)
#define TYPE_LOUDNESSLH1_LEVEL1                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS0                 12
#define FIXPT_LOUDNESSLH1_COEFFICIENTS0                0x00333932
#define VALUE_LOUDNESSLH1_COEFFICIENTS0                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS0                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS1                 13
#define FIXPT_LOUDNESSLH1_COEFFICIENTS1                0xFFCCC6CE
#define VALUE_LOUDNESSLH1_COEFFICIENTS1                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS1                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS2                 14
#define FIXPT_LOUDNESSLH1_COEFFICIENTS2                0x00333932
#define VALUE_LOUDNESSLH1_COEFFICIENTS2                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS2                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS3                 15
#define FIXPT_LOUDNESSLH1_COEFFICIENTS3                0x0000805C
#define VALUE_LOUDNESSLH1_COEFFICIENTS3                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.00391730721453343)
#define TYPE_LOUDNESSLH1_COEFFICIENTS3                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS4                 16
#define FIXPT_LOUDNESSLH1_COEFFICIENTS4                0x007F7FA3
#define VALUE_LOUDNESSLH1_COEFFICIENTS4                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.996082692785467)
#define TYPE_LOUDNESSLH1_COEFFICIENTS4                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_TARGET                        17
#define FIXPT_LOUDNESSLH1_TARGET                       0x00081385
#define VALUE_LOUDNESSLH1_TARGET                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0630957344480193)
#define TYPE_LOUDNESSLH1_TARGET                        SIGMASTUDIOTYPE_FIXPOINT

/* Module Surround1 - Surround Sound Volume Control*/
#define COUNT_SURROUND1                                9
#define DEVICE_SURROUND1                               "IC1"
#define ADDR_SURROUND1                                 18
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 18
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 18
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 19
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 19
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 19
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 20
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 20
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 20
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT

/* Module Bass Boost1 - Dynamic Bass Boost*/
#define COUNT_BASSBOOST1                               40
#define DEVICE_BASSBOOST1                              "IC1"
#define ADDR_BASSBOOST1_BASSFREQUENCY                  21
#define FIXPT_BASSBOOST1_BASSFREQUENCY                 0x0002430D
#define VALUE_BASSBOOST1_BASSFREQUENCY                 SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0176712287441837)
#define TYPE_BASSBOOST1_BASSFREQUENCY                  SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_B0                             22
#define FIXPT_BASSBOOST1_B0                            0x00000892
#define VALUE_BASSBOOST1_B0                            SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000261651801447982)
#define TYPE_BASSBOOST1_B0                             SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_B1                             23
#define FIXPT_BASSBOOST1_B1                            0x00001125
#define VALUE_BASSBOOST1_B1                            SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000523303602895963)
#define TYPE_BASSBOOST1_B1                             SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_B2                             24
#define FIXPT_BASSBOOST1_B2                            0x00000892
#define VALUE_BASSBOOST1_B2                            SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000261651801447982)
#define TYPE_BASSBOOST1_B2                             SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_A1                             25
#define FIXPT_BASSBOOST1_A1                            0x00FA1389
#define VALUE_BASSBOOST1_A1                            SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.95372127660762)
#define TYPE_BASSBOOST1_A1                             SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_A2                             26
#define FIXPT_BASSBOOST1_A2                            0xFF85CA2B
#define VALUE_BASSBOOST1_A2                            SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.954767883813409)
#define TYPE_BASSBOOST1_A2                             SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE0                         27
#define FIXPT_BASSBOOST1_TABLE0                        0x00299C75
#define VALUE_BASSBOOST1_TABLE0                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE0                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE1                         28
#define FIXPT_BASSBOOST1_TABLE1                        0x00299C75
#define VALUE_BASSBOOST1_TABLE1                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE1                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE2                         29
#define FIXPT_BASSBOOST1_TABLE2                        0x00299C75
#define VALUE_BASSBOOST1_TABLE2                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE2                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE3                         30
#define FIXPT_BASSBOOST1_TABLE3                        0x00299C75
#define VALUE_BASSBOOST1_TABLE3                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE3                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE4                         31
#define FIXPT_BASSBOOST1_TABLE4                        0x00299C75
#define VALUE_BASSBOOST1_TABLE4                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE4                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE5                         32
#define FIXPT_BASSBOOST1_TABLE5                        0x00299C75
#define VALUE_BASSBOOST1_TABLE5                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE5                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE6                         33
#define FIXPT_BASSBOOST1_TABLE6                        0x00299C75
#define VALUE_BASSBOOST1_TABLE6                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE6                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE7                         34
#define FIXPT_BASSBOOST1_TABLE7                        0x00299C75
#define VALUE_BASSBOOST1_TABLE7                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE7                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE8                         35
#define FIXPT_BASSBOOST1_TABLE8                        0x00299C75
#define VALUE_BASSBOOST1_TABLE8                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE8                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE9                         36
#define FIXPT_BASSBOOST1_TABLE9                        0x00299C75
#define VALUE_BASSBOOST1_TABLE9                        SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE9                         SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE10                        37
#define FIXPT_BASSBOOST1_TABLE10                       0x00299C75
#define VALUE_BASSBOOST1_TABLE10                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE10                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE11                        38
#define FIXPT_BASSBOOST1_TABLE11                       0x00299C75
#define VALUE_BASSBOOST1_TABLE11                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE11                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE12                        39
#define FIXPT_BASSBOOST1_TABLE12                       0x00299C75
#define VALUE_BASSBOOST1_TABLE12                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE12                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE13                        40
#define FIXPT_BASSBOOST1_TABLE13                       0x00299C75
#define VALUE_BASSBOOST1_TABLE13                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE13                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE14                        41
#define FIXPT_BASSBOOST1_TABLE14                       0x00299C75
#define VALUE_BASSBOOST1_TABLE14                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE14                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE15                        42
#define FIXPT_BASSBOOST1_TABLE15                       0x00299C75
#define VALUE_BASSBOOST1_TABLE15                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE15                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE16                        43
#define FIXPT_BASSBOOST1_TABLE16                       0x00299C75
#define VALUE_BASSBOOST1_TABLE16                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE16                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE17                        44
#define FIXPT_BASSBOOST1_TABLE17                       0x00299C75
#define VALUE_BASSBOOST1_TABLE17                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE17                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE18                        45
#define FIXPT_BASSBOOST1_TABLE18                       0x00299C75
#define VALUE_BASSBOOST1_TABLE18                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE18                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE19                        46
#define FIXPT_BASSBOOST1_TABLE19                       0x00299C75
#define VALUE_BASSBOOST1_TABLE19                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE19                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE20                        47
#define FIXPT_BASSBOOST1_TABLE20                       0x00299C75
#define VALUE_BASSBOOST1_TABLE20                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE20                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE21                        48
#define FIXPT_BASSBOOST1_TABLE21                       0x00299C75
#define VALUE_BASSBOOST1_TABLE21                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE21                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE22                        49
#define FIXPT_BASSBOOST1_TABLE22                       0x00299C75
#define VALUE_BASSBOOST1_TABLE22                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE22                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE23                        50
#define FIXPT_BASSBOOST1_TABLE23                       0x00299C75
#define VALUE_BASSBOOST1_TABLE23                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.325087297385434)
#define TYPE_BASSBOOST1_TABLE23                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE24                        51
#define FIXPT_BASSBOOST1_TABLE24                       0x003462A7
#define VALUE_BASSBOOST1_TABLE24                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.409260659730011)
#define TYPE_BASSBOOST1_TABLE24                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE25                        52
#define FIXPT_BASSBOOST1_TABLE25                       0x006885C5
#define VALUE_BASSBOOST1_TABLE25                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.816582371358592)
#define TYPE_BASSBOOST1_TABLE25                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE26                        53
#define FIXPT_BASSBOOST1_TABLE26                       0x00D08CC5
#define VALUE_BASSBOOST1_TABLE26                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.62929603263972)
#define TYPE_BASSBOOST1_TABLE26                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE27                        54
#define FIXPT_BASSBOOST1_TABLE27                       0x00E39EA8
#define VALUE_BASSBOOST1_TABLE27                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.77827941003892)
#define TYPE_BASSBOOST1_TABLE27                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE28                        55
#define FIXPT_BASSBOOST1_TABLE28                       0x00E39EA8
#define VALUE_BASSBOOST1_TABLE28                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.77827941003892)
#define TYPE_BASSBOOST1_TABLE28                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE29                        56
#define FIXPT_BASSBOOST1_TABLE29                       0x00E39EA8
#define VALUE_BASSBOOST1_TABLE29                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.77827941003892)
#define TYPE_BASSBOOST1_TABLE29                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE30                        57
#define FIXPT_BASSBOOST1_TABLE30                       0x00E39EA8
#define VALUE_BASSBOOST1_TABLE30                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.77827941003892)
#define TYPE_BASSBOOST1_TABLE30                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE31                        58
#define FIXPT_BASSBOOST1_TABLE31                       0x00E39EA8
#define VALUE_BASSBOOST1_TABLE31                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.77827941003892)
#define TYPE_BASSBOOST1_TABLE31                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TABLE32                        59
#define FIXPT_BASSBOOST1_TABLE32                       0x00E39EA8
#define VALUE_BASSBOOST1_TABLE32                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.77827941003892)
#define TYPE_BASSBOOST1_TABLE32                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_BASSBOOST1_TIMECONSTANT                   60
#define FIXPT_BASSBOOST1_TIMECONSTANT                  0x000006D3
#define VALUE_BASSBOOST1_TIMECONSTANT                  SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000208311633451363)
#define TYPE_BASSBOOST1_TIMECONSTANT                   SIGMASTUDIOTYPE_FIXPOINT

/* Module ReadBack1 - DSP Readback*/
#define COUNT_READBACK1                                2
#define DEVICE_READBACK1                               "IC1"
#define ADDR_READBACK1_VAL0                            2074
#define VALUES_READBACK1_VAL0                          SIGMASTUDIOTYPE_SPECIAL(0x027A)
#define TYPE_READBACK1_VAL0                            SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_VAL0                   0
#define ADDR_READBACK1_VAL1                            2074
#define VALUE_READBACK1_VAL1                           SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_VAL1                            SIGMASTUDIOTYPE_5_19

/* Module ReadBack_L - DSP Readback*/
#define COUNT_READBACK_L                               2
#define DEVICE_READBACK_L                              "IC1"
#define ADDR_READBACK_L_VAL0                           2074
#define VALUES_READBACK_L_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x0306)
#define TYPE_READBACK_L_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_L_VAL0                  0
#define ADDR_READBACK_L_VAL1                           2074
#define VALUE_READBACK_L_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_L_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module ReadBack1_2 - DSP Readback*/
#define COUNT_READBACK1_2                              2
#define DEVICE_READBACK1_2                             "IC1"
#define ADDR_READBACK1_2_VAL0                          2074
#define VALUES_READBACK1_2_VAL0                        SIGMASTUDIOTYPE_SPECIAL(0x0286)
#define TYPE_READBACK1_2_VAL0                          SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_2_VAL0                 0
#define ADDR_READBACK1_2_VAL1                          2074
#define VALUE_READBACK1_2_VAL1                         SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_2_VAL1                          SIGMASTUDIOTYPE_5_19

/* Module ReadBack_R - DSP Readback*/
#define COUNT_READBACK_R                               2
#define DEVICE_READBACK_R                              "IC1"
#define ADDR_READBACK_R_VAL0                           2074
#define VALUES_READBACK_R_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x02FA)
#define TYPE_READBACK_R_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_R_VAL0                  0
#define ADDR_READBACK_R_VAL1                           2074
#define VALUE_READBACK_R_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_R_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module Room_noice_value - DSP Readback*/
#define COUNT_ROOM_NOICE_VALUE                         2
#define DEVICE_ROOM_NOICE_VALUE                        "IC1"
#define ADDR_ROOM_NOICE_VALUE_VAL0                     2074
#define VALUES_ROOM_NOICE_VALUE_VAL0                   SIGMASTUDIOTYPE_SPECIAL(0x02AA)
#define TYPE_ROOM_NOICE_VALUE_VAL0                     SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_ROOM_NOICE_VALUE_VAL0            0
#define ADDR_ROOM_NOICE_VALUE_VAL1                     2074
#define VALUE_ROOM_NOICE_VALUE_VAL1                    SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_ROOM_NOICE_VALUE_VAL1                     SIGMASTUDIOTYPE_5_19

/* Module ReadBack1_3 - DSP Readback*/
#define COUNT_READBACK1_3                              2
#define DEVICE_READBACK1_3                             "IC1"
#define ADDR_READBACK1_3_VAL0                          2074
#define VALUES_READBACK1_3_VAL0                        SIGMASTUDIOTYPE_SPECIAL(0x0292)
#define TYPE_READBACK1_3_VAL0                          SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_3_VAL0                 0
#define ADDR_READBACK1_3_VAL1                          2074
#define VALUE_READBACK1_3_VAL1                         SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_3_VAL1                          SIGMASTUDIOTYPE_5_19

/* Module ReadBack1_4 - DSP Readback*/
#define COUNT_READBACK1_4                              2
#define DEVICE_READBACK1_4                             "IC1"
#define ADDR_READBACK1_4_VAL0                          2074
#define VALUES_READBACK1_4_VAL0                        SIGMASTUDIOTYPE_SPECIAL(0x029E)
#define TYPE_READBACK1_4_VAL0                          SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_4_VAL0                 0
#define ADDR_READBACK1_4_VAL1                          2074
#define VALUE_READBACK1_4_VAL1                         SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_4_VAL1                          SIGMASTUDIOTYPE_5_19

#endif
