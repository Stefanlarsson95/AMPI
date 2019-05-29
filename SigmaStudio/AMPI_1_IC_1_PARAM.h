/*
 * File:           C:\Users\Stefan\PycharmProjects\AMPI\SigmaStudio\AMPI_1_IC_1_PARAM.h
 *
 * Created:        Saturday, May 25, 2019 2:10:31 PM
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
#define FIXPT_MIX_AUX_RPI_OUT_STEREOSWSLEW             0x00000000
#define VALUE_MIX_AUX_RPI_OUT_STEREOSWSLEW             SIGMASTUDIOTYPE_INTEGER_CONVERT(0)
#define TYPE_MIX_AUX_RPI_OUT_STEREOSWSLEW              SIGMASTUDIOTYPE_INTEGER

/* Module Mix_Aux_Mic_IN - Stereo Switch Nx2*/
#define COUNT_MIX_AUX_MIC_IN                           1
#define DEVICE_MIX_AUX_MIC_IN                          "IC1"
#define ADDR_MIX_AUX_MIC_IN_STEREOSWSLEW               3
#define FIXPT_MIX_AUX_MIC_IN_STEREOSWSLEW              0x00000001
#define VALUE_MIX_AUX_MIC_IN_STEREOSWSLEW              SIGMASTUDIOTYPE_INTEGER_CONVERT(1)
#define TYPE_MIX_AUX_MIC_IN_STEREOSWSLEW               SIGMASTUDIOTYPE_INTEGER

/* Module Param EQ1 - Parametric EQ*/
#define COUNT_PARAMEQ1                                 30
#define DEVICE_PARAMEQ1                                "IC1"
#define ADDR_PARAMEQ1_ST0_B0                           4
#define FIXPT_PARAMEQ1_ST0_B0                          0x008962DD
#define VALUE_PARAMEQ1_ST0_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.07332962979475)
#define TYPE_PARAMEQ1_ST0_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B0                           4
#define FIXPT_PARAMEQ1_ST0_B0                          0x008962DD
#define VALUE_PARAMEQ1_ST0_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.07332962979475)
#define TYPE_PARAMEQ1_ST0_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B1                           5
#define FIXPT_PARAMEQ1_ST0_B1                          0xFEEE4BB3
#define VALUE_PARAMEQ1_ST0_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-2.13831492717801)
#define TYPE_PARAMEQ1_ST0_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B1                           5
#define FIXPT_PARAMEQ1_ST0_B1                          0xFEEE4BB3
#define VALUE_PARAMEQ1_ST0_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-2.13831492717801)
#define TYPE_PARAMEQ1_ST0_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B2                           6
#define FIXPT_PARAMEQ1_ST0_B2                          0x008853C8
#define VALUE_PARAMEQ1_ST0_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.06505686080218)
#define TYPE_PARAMEQ1_ST0_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_B2                           6
#define FIXPT_PARAMEQ1_ST0_B2                          0x008853C8
#define VALUE_PARAMEQ1_ST0_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.06505686080218)
#define TYPE_PARAMEQ1_ST0_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A0                           7
#define FIXPT_PARAMEQ1_ST0_A0                          0x00FF6F8B
#define VALUE_PARAMEQ1_ST0_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.99559160224728)
#define TYPE_PARAMEQ1_ST0_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A0                           7
#define FIXPT_PARAMEQ1_ST0_A0                          0x00FF6F8B
#define VALUE_PARAMEQ1_ST0_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.99559160224728)
#define TYPE_PARAMEQ1_ST0_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A1                           8
#define FIXPT_PARAMEQ1_ST0_A1                          0xFF808E45
#define VALUE_PARAMEQ1_ST0_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.995658389115774)
#define TYPE_PARAMEQ1_ST0_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST0_A1                           8
#define FIXPT_PARAMEQ1_ST0_A1                          0xFF808E45
#define VALUE_PARAMEQ1_ST0_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.995658389115774)
#define TYPE_PARAMEQ1_ST0_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B0                           9
#define FIXPT_PARAMEQ1_ST1_B0                          0x0076D87A
#define VALUE_PARAMEQ1_ST1_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.928481369167832)
#define TYPE_PARAMEQ1_ST1_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B0                           9
#define FIXPT_PARAMEQ1_ST1_B0                          0x0076D87A
#define VALUE_PARAMEQ1_ST1_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.928481369167832)
#define TYPE_PARAMEQ1_ST1_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B1                           10
#define FIXPT_PARAMEQ1_ST1_B1                          0x0032084B
#define VALUE_PARAMEQ1_ST1_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.390878175440666)
#define TYPE_PARAMEQ1_ST1_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B1                           10
#define FIXPT_PARAMEQ1_ST1_B1                          0x0032084B
#define VALUE_PARAMEQ1_ST1_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.390878175440666)
#define TYPE_PARAMEQ1_ST1_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B2                           11
#define FIXPT_PARAMEQ1_ST1_B2                          0x004A76FA
#define VALUE_PARAMEQ1_ST1_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.581755929195725)
#define TYPE_PARAMEQ1_ST1_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_B2                           11
#define FIXPT_PARAMEQ1_ST1_B2                          0x004A76FA
#define VALUE_PARAMEQ1_ST1_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.581755929195725)
#define TYPE_PARAMEQ1_ST1_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A0                           12
#define FIXPT_PARAMEQ1_ST1_A0                          0xFFCDF7B5
#define VALUE_PARAMEQ1_ST1_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.390878175440666)
#define TYPE_PARAMEQ1_ST1_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A0                           12
#define FIXPT_PARAMEQ1_ST1_A0                          0xFFCDF7B5
#define VALUE_PARAMEQ1_ST1_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.390878175440666)
#define TYPE_PARAMEQ1_ST1_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A1                           13
#define FIXPT_PARAMEQ1_ST1_A1                          0xFFBEB08C
#define VALUE_PARAMEQ1_ST1_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.510237298363556)
#define TYPE_PARAMEQ1_ST1_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST1_A1                           13
#define FIXPT_PARAMEQ1_ST1_A1                          0xFFBEB08C
#define VALUE_PARAMEQ1_ST1_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.510237298363556)
#define TYPE_PARAMEQ1_ST1_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B0                           14
#define FIXPT_PARAMEQ1_ST2_B0                          0x0071BFB6
#define VALUE_PARAMEQ1_ST2_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.888663152418509)
#define TYPE_PARAMEQ1_ST2_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B0                           14
#define FIXPT_PARAMEQ1_ST2_B0                          0x0071BFB6
#define VALUE_PARAMEQ1_ST2_B0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.888663152418509)
#define TYPE_PARAMEQ1_ST2_B0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B1                           15
#define FIXPT_PARAMEQ1_ST2_B1                          0xFF1F34DE
#define VALUE_PARAMEQ1_ST2_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-1.75619917874997)
#define TYPE_PARAMEQ1_ST2_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B1                           15
#define FIXPT_PARAMEQ1_ST2_B1                          0xFF1F34DE
#define VALUE_PARAMEQ1_ST2_B1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-1.75619917874997)
#define TYPE_PARAMEQ1_ST2_B1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B2                           16
#define FIXPT_PARAMEQ1_ST2_B2                          0x006F30B9
#define VALUE_PARAMEQ1_ST2_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.868674494701951)
#define TYPE_PARAMEQ1_ST2_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_B2                           16
#define FIXPT_PARAMEQ1_ST2_B2                          0x006F30B9
#define VALUE_PARAMEQ1_ST2_B2                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.868674494701951)
#define TYPE_PARAMEQ1_ST2_B2                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A0                           17
#define FIXPT_PARAMEQ1_ST2_A0                          0x00FC38F2
#define VALUE_PARAMEQ1_ST2_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.97048788798742)
#define TYPE_PARAMEQ1_ST2_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A0                           17
#define FIXPT_PARAMEQ1_ST2_A0                          0x00FC38F2
#define VALUE_PARAMEQ1_ST2_A0                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.97048788798742)
#define TYPE_PARAMEQ1_ST2_A0                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A1                           18
#define FIXPT_PARAMEQ1_ST2_A1                          0xFF839D33
#define VALUE_PARAMEQ1_ST2_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.971765270508749)
#define TYPE_PARAMEQ1_ST2_A1                           SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_PARAMEQ1_ST2_A1                           18
#define FIXPT_PARAMEQ1_ST2_A1                          0xFF839D33
#define VALUE_PARAMEQ1_ST2_A1                          SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.971765270508749)
#define TYPE_PARAMEQ1_ST2_A1                           SIGMASTUDIOTYPE_FIXPOINT

/* Module Loudness L&H1 - Loudness (Low & Hi)*/
#define COUNT_LOUDNESSLH1                              8
#define DEVICE_LOUDNESSLH1                             "IC1"
#define ADDR_LOUDNESSLH1_LEVEL0                        19
#define FIXPT_LOUDNESSLH1_LEVEL0                       0x011C28F5
#define VALUE_LOUDNESSLH1_LEVEL0                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(2.22)
#define TYPE_LOUDNESSLH1_LEVEL0                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_LEVEL1                        20
#define FIXPT_LOUDNESSLH1_LEVEL1                       0x012147AE
#define VALUE_LOUDNESSLH1_LEVEL1                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(2.26)
#define TYPE_LOUDNESSLH1_LEVEL1                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS0                 21
#define FIXPT_LOUDNESSLH1_COEFFICIENTS0                0x00333932
#define VALUE_LOUDNESSLH1_COEFFICIENTS0                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS0                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS1                 22
#define FIXPT_LOUDNESSLH1_COEFFICIENTS1                0xFFCCC6CE
#define VALUE_LOUDNESSLH1_COEFFICIENTS1                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS1                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS2                 23
#define FIXPT_LOUDNESSLH1_COEFFICIENTS2                0x00333932
#define VALUE_LOUDNESSLH1_COEFFICIENTS2                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.400183005102475)
#define TYPE_LOUDNESSLH1_COEFFICIENTS2                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS3                 24
#define FIXPT_LOUDNESSLH1_COEFFICIENTS3                0x00010038
#define VALUE_LOUDNESSLH1_COEFFICIENTS3                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.00781926913325381)
#define TYPE_LOUDNESSLH1_COEFFICIENTS3                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS4                 25
#define FIXPT_LOUDNESSLH1_COEFFICIENTS4                0x007EFFC7
#define VALUE_LOUDNESSLH1_COEFFICIENTS4                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.992180730866746)
#define TYPE_LOUDNESSLH1_COEFFICIENTS4                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_TARGET                        26
#define FIXPT_LOUDNESSLH1_TARGET                       0x00198A13
#define VALUE_LOUDNESSLH1_TARGET                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.199526231496888)
#define TYPE_LOUDNESSLH1_TARGET                        SIGMASTUDIOTYPE_FIXPOINT

/* Module SW vol 1 - Single slew ext vol*/
#define COUNT_SWVOL1                                   1
#define DEVICE_SWVOL1                                  "IC1"
#define ADDR_SWVOL1_STEP                               27
#define FIXPT_SWVOL1_STEP                              0x00000800
#define VALUE_SWVOL1_STEP                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000244140625)
#define TYPE_SWVOL1_STEP                               SIGMASTUDIOTYPE_FIXPOINT

/* Module Multiple 1 - Multiple Volume Control*/
#define COUNT_MULTIPLE1                                2
#define DEVICE_MULTIPLE1                               "IC1"
#define ADDR_MULTIPLE1                                 28
#define FIXPT_MULTIPLE1                                0x00800000
#define VALUE_MULTIPLE1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_MULTIPLE1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_MULTIPLE1_1                               29
#define FIXPT_MULTIPLE1_1                              0x00A12477
#define VALUE_MULTIPLE1_1                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.25892541179417)
#define TYPE_MULTIPLE1_1                               SIGMASTUDIOTYPE_FIXPOINT

/* Module Gen Filter1_2 - General (2nd order)*/
#define COUNT_GENFILTER1_2                             5
#define DEVICE_GENFILTER1_2                            "IC1"
#define ADDR_GENFILTER1_2_ST0_B0                       30
#define FIXPT_GENFILTER1_2_ST0_B0                      0x00058026
#define VALUE_GENFILTER1_2_ST0_B0                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.042973364483739)
#define TYPE_GENFILTER1_2_ST0_B0                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_B1                       31
#define FIXPT_GENFILTER1_2_ST0_B1                      0x00000000
#define VALUE_GENFILTER1_2_ST0_B1                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_GENFILTER1_2_ST0_B1                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_B2                       32
#define FIXPT_GENFILTER1_2_ST0_B2                      0xFFFA7FDA
#define VALUE_GENFILTER1_2_ST0_B2                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.042973364483739)
#define TYPE_GENFILTER1_2_ST0_B2                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_A1                       33
#define FIXPT_GENFILTER1_2_ST0_A1                      0x00F47968
#define VALUE_GENFILTER1_2_ST0_A1                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.90995513605384)
#define TYPE_GENFILTER1_2_ST0_A1                       SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_GENFILTER1_2_ST0_A2                       34
#define FIXPT_GENFILTER1_2_ST0_A2                      0xFF8B004E
#define VALUE_GENFILTER1_2_ST0_A2                      SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-0.914053271032522)
#define TYPE_GENFILTER1_2_ST0_A2                       SIGMASTUDIOTYPE_FIXPOINT

/* Module Surround1 - Surround Sound Volume Control*/
#define COUNT_SURROUND1                                9
#define DEVICE_SURROUND1                               "IC1"
#define ADDR_SURROUND1                                 35
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 35
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 35
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 36
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 36
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 36
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253519425)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 37
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 37
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SURROUND1                                 37
#define FIXPT_SURROUND1                                0x00C858E2
#define VALUE_SURROUND1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.56521253527117)
#define TYPE_SURROUND1                                 SIGMASTUDIOTYPE_FIXPOINT

/* Module DCB1 - DC Blocking*/
#define COUNT_DCB1                                     2
#define DEVICE_DCB1                                    "IC1"
#define ADDR_DCB1_POLE                                 38
#define FIXPT_DCB1_POLE                                0x007FFCB9
#define VALUE_DCB1_POLE                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.9999)
#define TYPE_DCB1_POLE                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_DCB1_1_POLE                               39
#define FIXPT_DCB1_1_POLE                              0x007FFCB9
#define VALUE_DCB1_1_POLE                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.9999)
#define TYPE_DCB1_1_POLE                               SIGMASTUDIOTYPE_FIXPOINT

/* Module ReadBack1 - DSP Readback*/
#define COUNT_READBACK1                                2
#define DEVICE_READBACK1                               "IC1"
#define ADDR_READBACK1_VAL0                            2074
#define VALUES_READBACK1_VAL0                          SIGMASTUDIOTYPE_SPECIAL(0x006A)
#define TYPE_READBACK1_VAL0                            SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_VAL0                   0
#define ADDR_READBACK1_VAL1                            2074
#define VALUE_READBACK1_VAL1                           SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_VAL1                            SIGMASTUDIOTYPE_5_19

/* Module ReadBack_L - DSP Readback*/
#define COUNT_READBACK_L                               2
#define DEVICE_READBACK_L                              "IC1"
#define ADDR_READBACK_L_VAL0                           2074
#define VALUES_READBACK_L_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x04E2)
#define TYPE_READBACK_L_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_L_VAL0                  0
#define ADDR_READBACK_L_VAL1                           2074
#define VALUE_READBACK_L_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_L_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module ReadBack_R - DSP Readback*/
#define COUNT_READBACK_R                               2
#define DEVICE_READBACK_R                              "IC1"
#define ADDR_READBACK_R_VAL0                           2074
#define VALUES_READBACK_R_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x04D6)
#define TYPE_READBACK_R_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_R_VAL0                  0
#define ADDR_READBACK_R_VAL1                           2074
#define VALUE_READBACK_R_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_R_VAL1                           SIGMASTUDIOTYPE_5_19

#endif
