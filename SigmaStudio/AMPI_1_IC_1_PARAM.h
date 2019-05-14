/*
 * File:           C:\Users\Stefan\PycharmProjects\AMPI\SigmaStudio\AMPI_1_IC_1_PARAM.h
 *
 * Created:        Friday, May 17, 2019 11:05:01 PM
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

/* Module Single 1 - Single Volume*/
#define COUNT_SINGLE1                                  2
#define DEVICE_SINGLE1                                 "IC1"
#define ADDR_SINGLE1                                   3
#define FIXPT_SINGLE1                                  0x00800000
#define VALUE_SINGLE1                                  SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_SINGLE1                                   SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SINGLE1_1                                 4
#define FIXPT_SINGLE1_1                                0x00800000
#define VALUE_SINGLE1_1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_SINGLE1_1                                 SIGMASTUDIOTYPE_FIXPOINT

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
#define FIXPT_LOUDNESSLH1_LEVEL0                       0x0111EB85
#define VALUE_LOUDNESSLH1_LEVEL0                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(2.14)
#define TYPE_LOUDNESSLH1_LEVEL0                        SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_LEVEL1                        11
#define FIXPT_LOUDNESSLH1_LEVEL1                       0x00FD70A3
#define VALUE_LOUDNESSLH1_LEVEL1                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1.98)
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
#define FIXPT_LOUDNESSLH1_COEFFICIENTS3                0x00010038
#define VALUE_LOUDNESSLH1_COEFFICIENTS3                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.00781926913325381)
#define TYPE_LOUDNESSLH1_COEFFICIENTS3                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_COEFFICIENTS4                 16
#define FIXPT_LOUDNESSLH1_COEFFICIENTS4                0x007EFFC7
#define VALUE_LOUDNESSLH1_COEFFICIENTS4                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.992180730866746)
#define TYPE_LOUDNESSLH1_COEFFICIENTS4                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_LOUDNESSLH1_TARGET                        17
#define FIXPT_LOUDNESSLH1_TARGET                       0x00144960
#define VALUE_LOUDNESSLH1_TARGET                       SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.158489319246111)
#define TYPE_LOUDNESSLH1_TARGET                        SIGMASTUDIOTYPE_FIXPOINT

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
