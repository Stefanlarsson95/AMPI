/*
 * File:           C:\Users\Stefan\PycharmProjects\AMPI\CASE_DSP\CASE_DSP_IC_1_PARAM.h
 *
 * Created:        Sunday, September 15, 2019 7:39:51 PM
 * Description:    CASE_DSP:IC 1 parameter RAM definitions.
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
#ifndef __CASE_DSP_IC_1_PARAM_H__
#define __CASE_DSP_IC_1_PARAM_H__


/* Module SorceEquGain - Gain*/
#define COUNT_SORCEEQUGAIN                             2
#define DEVICE_SORCEEQUGAIN                            "IC1"
#define ADDR_SORCEEQUGAIN                              0
#define FIXPT_SORCEEQUGAIN                             0x03400000
#define VALUE_SORCEEQUGAIN                             SIGMASTUDIOTYPE_FIXPOINT_CONVERT(6.5)
#define TYPE_SORCEEQUGAIN                              SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SORCEEQUGAIN_1                            1
#define FIXPT_SORCEEQUGAIN_1                           0x03400000
#define VALUE_SORCEEQUGAIN_1                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(6.5)
#define TYPE_SORCEEQUGAIN_1                            SIGMASTUDIOTYPE_FIXPOINT

/* Module Mix_Aux_Rpi_OUT - Stereo Switch Nx2*/
#define COUNT_MIX_AUX_RPI_OUT                          1
#define DEVICE_MIX_AUX_RPI_OUT                         "IC1"
#define ADDR_MIX_AUX_RPI_OUT_STEREOSWSLEW              2
#define FIXPT_MIX_AUX_RPI_OUT_STEREOSWSLEW             0x00000001
#define VALUE_MIX_AUX_RPI_OUT_STEREOSWSLEW             SIGMASTUDIOTYPE_INTEGER_CONVERT(1)
#define TYPE_MIX_AUX_RPI_OUT_STEREOSWSLEW              SIGMASTUDIOTYPE_INTEGER

/* Module Param EQ1 - Parametric EQ*/
#define COUNT_PARAMEQ1                                 30
#define DEVICE_PARAMEQ1                                "IC1"
#define ADDR_PARAMEQ1_ST0_B0                           3
#define FIXPT_PARAMEQ1_ST0_B0                          0x008962DD
#define VALUE_PARAMEQ1_ST0_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.07332962979475)
#define TYPE_PARAMEQ1_ST0_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B0                           3
#define FIXPT_PARAMEQ1_ST0_B0                          0x008962DD
#define VALUE_PARAMEQ1_ST0_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.07332962979475)
#define TYPE_PARAMEQ1_ST0_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B1                           4
#define FIXPT_PARAMEQ1_ST0_B1                          0xFEEE4BB3
#define VALUE_PARAMEQ1_ST0_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-2.13831492717801)
#define TYPE_PARAMEQ1_ST0_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B1                           4
#define FIXPT_PARAMEQ1_ST0_B1                          0xFEEE4BB3
#define VALUE_PARAMEQ1_ST0_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-2.13831492717801)
#define TYPE_PARAMEQ1_ST0_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B2                           5
#define FIXPT_PARAMEQ1_ST0_B2                          0x008853C8
#define VALUE_PARAMEQ1_ST0_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.06505686080218)
#define TYPE_PARAMEQ1_ST0_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B2                           5
#define FIXPT_PARAMEQ1_ST0_B2                          0x008853C8
#define VALUE_PARAMEQ1_ST0_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.06505686080218)
#define TYPE_PARAMEQ1_ST0_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A0                           6
#define FIXPT_PARAMEQ1_ST0_A0                          0x00FF6F8B
#define VALUE_PARAMEQ1_ST0_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.99559160224728)
#define TYPE_PARAMEQ1_ST0_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A0                           6
#define FIXPT_PARAMEQ1_ST0_A0                          0x00FF6F8B
#define VALUE_PARAMEQ1_ST0_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.99559160224728)
#define TYPE_PARAMEQ1_ST0_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A1                           7
#define FIXPT_PARAMEQ1_ST0_A1                          0xFF808E45
#define VALUE_PARAMEQ1_ST0_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.995658389115774)
#define TYPE_PARAMEQ1_ST0_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A1                           7
#define FIXPT_PARAMEQ1_ST0_A1                          0xFF808E45
#define VALUE_PARAMEQ1_ST0_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.995658389115774)
#define TYPE_PARAMEQ1_ST0_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B0                           8
#define FIXPT_PARAMEQ1_ST1_B0                          0x0076D87A
#define VALUE_PARAMEQ1_ST1_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.928481369167832)
#define TYPE_PARAMEQ1_ST1_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B0                           8
#define FIXPT_PARAMEQ1_ST1_B0                          0x0076D87A
#define VALUE_PARAMEQ1_ST1_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.928481369167832)
#define TYPE_PARAMEQ1_ST1_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B1                           9
#define FIXPT_PARAMEQ1_ST1_B1                          0x0032084B
#define VALUE_PARAMEQ1_ST1_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.390878175440666)
#define TYPE_PARAMEQ1_ST1_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B1                           9
#define FIXPT_PARAMEQ1_ST1_B1                          0x0032084B
#define VALUE_PARAMEQ1_ST1_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.390878175440666)
#define TYPE_PARAMEQ1_ST1_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B2                           10
#define FIXPT_PARAMEQ1_ST1_B2                          0x004A76FA
#define VALUE_PARAMEQ1_ST1_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.581755929195725)
#define TYPE_PARAMEQ1_ST1_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B2                           10
#define FIXPT_PARAMEQ1_ST1_B2                          0x004A76FA
#define VALUE_PARAMEQ1_ST1_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.581755929195725)
#define TYPE_PARAMEQ1_ST1_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A0                           11
#define FIXPT_PARAMEQ1_ST1_A0                          0xFFCDF7B5
#define VALUE_PARAMEQ1_ST1_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.390878175440666)
#define TYPE_PARAMEQ1_ST1_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A0                           11
#define FIXPT_PARAMEQ1_ST1_A0                          0xFFCDF7B5
#define VALUE_PARAMEQ1_ST1_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.390878175440666)
#define TYPE_PARAMEQ1_ST1_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A1                           12
#define FIXPT_PARAMEQ1_ST1_A1                          0xFFBEB08C
#define VALUE_PARAMEQ1_ST1_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.510237298363556)
#define TYPE_PARAMEQ1_ST1_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A1                           12
#define FIXPT_PARAMEQ1_ST1_A1                          0xFFBEB08C
#define VALUE_PARAMEQ1_ST1_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.510237298363556)
#define TYPE_PARAMEQ1_ST1_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B0                           13
#define FIXPT_PARAMEQ1_ST2_B0                          0x0071BFB6
#define VALUE_PARAMEQ1_ST2_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.888663152418509)
#define TYPE_PARAMEQ1_ST2_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B0                           13
#define FIXPT_PARAMEQ1_ST2_B0                          0x0071BFB6
#define VALUE_PARAMEQ1_ST2_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.888663152418509)
#define TYPE_PARAMEQ1_ST2_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B1                           14
#define FIXPT_PARAMEQ1_ST2_B1                          0xFF1F34DE
#define VALUE_PARAMEQ1_ST2_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-1.75619917874997)
#define TYPE_PARAMEQ1_ST2_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B1                           14
#define FIXPT_PARAMEQ1_ST2_B1                          0xFF1F34DE
#define VALUE_PARAMEQ1_ST2_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-1.75619917874997)
#define TYPE_PARAMEQ1_ST2_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B2                           15
#define FIXPT_PARAMEQ1_ST2_B2                          0x006F30B9
#define VALUE_PARAMEQ1_ST2_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.868674494701951)
#define TYPE_PARAMEQ1_ST2_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B2                           15
#define FIXPT_PARAMEQ1_ST2_B2                          0x006F30B9
#define VALUE_PARAMEQ1_ST2_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.868674494701951)
#define TYPE_PARAMEQ1_ST2_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A0                           16
#define FIXPT_PARAMEQ1_ST2_A0                          0x00FC38F2
#define VALUE_PARAMEQ1_ST2_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.97048788798742)
#define TYPE_PARAMEQ1_ST2_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A0                           16
#define FIXPT_PARAMEQ1_ST2_A0                          0x00FC38F2
#define VALUE_PARAMEQ1_ST2_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.97048788798742)
#define TYPE_PARAMEQ1_ST2_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A1                           17
#define FIXPT_PARAMEQ1_ST2_A1                          0xFF839D33
#define VALUE_PARAMEQ1_ST2_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.971765270508749)
#define TYPE_PARAMEQ1_ST2_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A1                           17
#define FIXPT_PARAMEQ1_ST2_A1                          0xFF839D33
#define VALUE_PARAMEQ1_ST2_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.971765270508749)
#define TYPE_PARAMEQ1_ST2_A1                           SIGMASTUDIOTYPE_FIXPOINT

/* Module Loudness L&H1 - Loudness (Low & Hi)*/
#define COUNT_LOUDNESSLH1                              8
#define DEVICE_LOUDNESSLH1                             "IC1"
#define ADDR_LOUDNESSLH1_LEVEL0                        18
#define FIXPT_LOUDNESSLH1_LEVEL0                       0x011C28F5
#define VALUE_LOUDNESSLH1_LEVEL0                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(2.22)
#define TYPE_LOUDNESSLH1_LEVEL0                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_LEVEL1                        19
#define FIXPT_LOUDNESSLH1_LEVEL1                       0x013AE147
#define VALUE_LOUDNESSLH1_LEVEL1                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(2.46)
#define TYPE_LOUDNESSLH1_LEVEL1                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS0                 20
#define FIXPT_LOUDNESSLH1_COEFFICIENTS0                0x00333932
#define VALUE_LOUDNESSLH1_COEFFICIENTS0                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS0                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS1                 21
#define FIXPT_LOUDNESSLH1_COEFFICIENTS1                0xFFCCC6CE
#define VALUE_LOUDNESSLH1_COEFFICIENTS1                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS1                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS2                 22
#define FIXPT_LOUDNESSLH1_COEFFICIENTS2                0x00333932
#define VALUE_LOUDNESSLH1_COEFFICIENTS2                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS2                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS3                 23
#define FIXPT_LOUDNESSLH1_COEFFICIENTS3                0x00010038
#define VALUE_LOUDNESSLH1_COEFFICIENTS3                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.00781926913325381)
#define TYPE_LOUDNESSLH1_COEFFICIENTS3                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS4                 24
#define FIXPT_LOUDNESSLH1_COEFFICIENTS4                0x007EFFC7
#define VALUE_LOUDNESSLH1_COEFFICIENTS4                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.992180730866746)
#define TYPE_LOUDNESSLH1_COEFFICIENTS4                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_TARGET                        25
#define FIXPT_LOUDNESSLH1_TARGET                       0x000A2ADA
#define VALUE_LOUDNESSLH1_TARGET                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0794328234724281)
#define TYPE_LOUDNESSLH1_TARGET                        SIGMASTUDIOTYPE_FIXPOINT

/* Module Gen Filter1_2 - General (2nd order)*/
#define COUNT_GENFILTER1_2                             5
#define DEVICE_GENFILTER1_2                            "IC1"
#define ADDR_GENFILTER1_2_ST0_B0                       26
#define FIXPT_GENFILTER1_2_ST0_B0                      0x0001144A
#define VALUE_GENFILTER1_2_ST0_B0                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.00843169457000996)
#define TYPE_GENFILTER1_2_ST0_B0                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_B1                       27
#define FIXPT_GENFILTER1_2_ST0_B1                      0x00022894
#define VALUE_GENFILTER1_2_ST0_B1                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0168633891400199)
#define TYPE_GENFILTER1_2_ST0_B1                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_B2                       28
#define FIXPT_GENFILTER1_2_ST0_B2                      0x0001144A
#define VALUE_GENFILTER1_2_ST0_B2                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.00843169457000996)
#define TYPE_GENFILTER1_2_ST0_B2                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_A1                       29
#define FIXPT_GENFILTER1_2_ST0_A1                      0x00F9EF0F
#define VALUE_GENFILTER1_2_ST0_A1                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.95260804759685)
#define TYPE_GENFILTER1_2_ST0_A1                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_A2                       30
#define FIXPT_GENFILTER1_2_ST0_A2                      0xFF854C6A
#define VALUE_GENFILTER1_2_ST0_A2                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.958605611135083)
#define TYPE_GENFILTER1_2_ST0_A2                       SIGMASTUDIOTYPE_FIXPOINT

/* Module Multiple 1 - Multiple Volume Control*/
#define COUNT_MULTIPLE1                                3
#define DEVICE_MULTIPLE1                               "IC1"
#define ADDR_MULTIPLE1                                 31
#define FIXPT_MULTIPLE1                                0x0050C335
#define VALUE_MULTIPLE1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.630957344480193)
#define TYPE_MULTIPLE1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_MULTIPLE1_1                               32
#define FIXPT_MULTIPLE1_1                              0x0050C335
#define VALUE_MULTIPLE1_1                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.630957344480193)
#define TYPE_MULTIPLE1_1                               SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_MULTIPLE1_2                               33
#define FIXPT_MULTIPLE1_2                              0x00A12477
#define VALUE_MULTIPLE1_2                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.25892541179417)
#define TYPE_MULTIPLE1_2                               SIGMASTUDIOTYPE_FIXPOINT

/* Module Surround1 - Surround Sound Volume Control*/
#define COUNT_SURROUND1                                9
#define DEVICE_SURROUND1                               "IC1"
#define ADDR_SURROUND1                                 34
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 34
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 34
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 35
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 35
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 35
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 36
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 36
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 36
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT

/* Module DCB1 - DC Blocking*/
#define COUNT_DCB1                                     2
#define DEVICE_DCB1                                    "IC1"
#define ADDR_DCB1_1_POLE                               37
#define FIXPT_DCB1_1_POLE                              0x007FFCB9
#define VALUE_DCB1_1_POLE                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.9999)
#define TYPE_DCB1_1_POLE                               SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_DCB1_POLE                                 38
#define FIXPT_DCB1_POLE                                0x007FFCB9
#define VALUE_DCB1_POLE                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.9999)
#define TYPE_DCB1_POLE                                 SIGMASTUDIOTYPE_FIXPOINT

/* Module ReadBack1 - DSP Readback*/
#define COUNT_READBACK1                                2
#define DEVICE_READBACK1                               "IC1"
#define ADDR_READBACK1_VAL0                            2074
#define VALUES_READBACK1_VAL0                          SIGMASTUDIOTYPE_SPECIAL(0x00A6)
#define TYPE_READBACK1_VAL0                            SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_VAL0                   0
#define ADDR_READBACK1_VAL1                            2074
#define VALUE_READBACK1_VAL1                           SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_VAL1                            SIGMASTUDIOTYPE_5_19

/* Module ReadBack_L - DSP Readback*/
#define COUNT_READBACK_L                               2
#define DEVICE_READBACK_L                              "IC1"
#define ADDR_READBACK_L_VAL0                           2074
#define VALUES_READBACK_L_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x03D2)
#define TYPE_READBACK_L_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_L_VAL0                  0
#define ADDR_READBACK_L_VAL1                           2074
#define VALUE_READBACK_L_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_L_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module ReadBack_R - DSP Readback*/
#define COUNT_READBACK_R                               2
#define DEVICE_READBACK_R                              "IC1"
#define ADDR_READBACK_R_VAL0                           2074
#define VALUES_READBACK_R_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x03C6)
#define TYPE_READBACK_R_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_R_VAL0                  0
#define ADDR_READBACK_R_VAL1                           2074
#define VALUE_READBACK_R_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_R_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module ReadBack_R_2 - DSP Readback*/
#define COUNT_READBACK_R_2                             2
#define DEVICE_READBACK_R_2                            "IC1"
#define ADDR_READBACK_R_2_VAL0                         2074
#define VALUES_READBACK_R_2_VAL0                       SIGMASTUDIOTYPE_SPECIAL(0x008E)
#define TYPE_READBACK_R_2_VAL0                         SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_R_2_VAL0                0
#define ADDR_READBACK_R_2_VAL1                         2074
#define VALUE_READBACK_R_2_VAL1                        SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_R_2_VAL1                         SIGMASTUDIOTYPE_5_19

/* Module ReadBack_L_2 - DSP Readback*/
#define COUNT_READBACK_L_2                             2
#define DEVICE_READBACK_L_2                            "IC1"
#define ADDR_READBACK_L_2_VAL0                         2074
#define VALUES_READBACK_L_2_VAL0                       SIGMASTUDIOTYPE_SPECIAL(0x0082)
#define TYPE_READBACK_L_2_VAL0                         SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_L_2_VAL0                0
#define ADDR_READBACK_L_2_VAL1                         2074
#define VALUE_READBACK_L_2_VAL1                        SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_L_2_VAL1                         SIGMASTUDIOTYPE_5_19

/* Module ReadBack_R_3 - DSP Readback*/
#define COUNT_READBACK_R_3                             2
#define DEVICE_READBACK_R_3                            "IC1"
#define ADDR_READBACK_R_3_VAL0                         2074
#define VALUES_READBACK_R_3_VAL0                       SIGMASTUDIOTYPE_SPECIAL(0x009A)
#define TYPE_READBACK_R_3_VAL0                         SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_R_3_VAL0                0
#define ADDR_READBACK_R_3_VAL1                         2074
#define VALUE_READBACK_R_3_VAL1                        SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_R_3_VAL1                         SIGMASTUDIOTYPE_5_19

#endif
