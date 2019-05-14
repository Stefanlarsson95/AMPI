/*
 * File:           C:\Users\Stefan\PycharmProjects\AMPI\SigmaStudio\AMPI_1_IC_1_PARAM.h
 *
 * Created:        Tuesday, May 14, 2019 8:58:07 PM
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


/* Module Mix_Aux_Mic - Stereo Switch Nx2*/
#define COUNT_MIX_AUX_MIC                              1
#define DEVICE_MIX_AUX_MIC                             "IC1"
#define ADDR_MIX_AUX_MIC_STEREOSWSLEW                  0
#define FIXPT_MIX_AUX_MIC_STEREOSWSLEW                 0x00000001
#define VALUE_MIX_AUX_MIC_STEREOSWSLEW                 SIGMASTUDIOTYPE_INTEGER_CONVERT(1)
#define TYPE_MIX_AUX_MIC_STEREOSWSLEW                  SIGMASTUDIOTYPE_INTEGER

/* Module SW vol 1 - Single slew ext vol*/
#define COUNT_SWVOL1                                   1
#define DEVICE_SWVOL1                                  "IC1"
#define ADDR_SWVOL1_STEP                               1
#define FIXPT_SWVOL1_STEP                              0x00000800
#define VALUE_SWVOL1_STEP                              SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000244140625)
#define TYPE_SWVOL1_STEP                               SIGMASTUDIOTYPE_FIXPOINT

/* Module Single 1 - Single Volume*/
#define COUNT_SINGLE1                                  2
#define DEVICE_SINGLE1                                 "IC1"
#define ADDR_SINGLE1                                   2
#define FIXPT_SINGLE1                                  0x00800000
#define VALUE_SINGLE1                                  SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_SINGLE1                                   SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SINGLE1_1                                 3
#define FIXPT_SINGLE1_1                                0x00800000
#define VALUE_SINGLE1_1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_SINGLE1_1                                 SIGMASTUDIOTYPE_FIXPOINT

/* Module SW vol 1_2 - Single slew ext vol*/
#define COUNT_SWVOL1_2                                 1
#define DEVICE_SWVOL1_2                                "IC1"
#define ADDR_SWVOL1_2_STEP                             4
#define FIXPT_SWVOL1_2_STEP                            0x00000800
#define VALUE_SWVOL1_2_STEP                            SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.000244140625)
#define TYPE_SWVOL1_2_STEP                             SIGMASTUDIOTYPE_FIXPOINT

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

/* Module ReadBack1_2 - DSP Readback*/
#define COUNT_READBACK1_2                              2
#define DEVICE_READBACK1_2                             "IC1"
#define ADDR_READBACK1_2_VAL0                          2074
#define VALUES_READBACK1_2_VAL0                        SIGMASTUDIOTYPE_SPECIAL(0x01BA)
#define TYPE_READBACK1_2_VAL0                          SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_2_VAL0                 0
#define ADDR_READBACK1_2_VAL1                          2074
#define VALUE_READBACK1_2_VAL1                         SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_2_VAL1                          SIGMASTUDIOTYPE_5_19

/* Module ReadBack_L - DSP Readback*/
#define COUNT_READBACK_L                               2
#define DEVICE_READBACK_L                              "IC1"
#define ADDR_READBACK_L_VAL0                           2074
#define VALUES_READBACK_L_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x016E)
#define TYPE_READBACK_L_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_L_VAL0                  0
#define ADDR_READBACK_L_VAL1                           2074
#define VALUE_READBACK_L_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_L_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module ReadBack_R - DSP Readback*/
#define COUNT_READBACK_R                               2
#define DEVICE_READBACK_R                              "IC1"
#define ADDR_READBACK_R_VAL0                           2074
#define VALUES_READBACK_R_VAL0                         SIGMASTUDIOTYPE_SPECIAL(0x0162)
#define TYPE_READBACK_R_VAL0                           SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK_R_VAL0                  0
#define ADDR_READBACK_R_VAL1                           2074
#define VALUE_READBACK_R_VAL1                          SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK_R_VAL1                           SIGMASTUDIOTYPE_5_19

/* Module ReadBack1 - DSP Readback*/
#define COUNT_READBACK1                                2
#define DEVICE_READBACK1                               "IC1"
#define ADDR_READBACK1_VAL0                            2074
#define VALUES_READBACK1_VAL0                          SIGMASTUDIOTYPE_SPECIAL(0x01AE)
#define TYPE_READBACK1_VAL0                            SIGMASTUDIOTYPE_SPECIAL
#define ADDR_READBACK_READBACK1_VAL0                   0
#define ADDR_READBACK1_VAL1                            2074
#define VALUE_READBACK1_VAL1                           SIGMASTUDIOTYPE_5_19_CONVERT(0)
#define TYPE_READBACK1_VAL1                            SIGMASTUDIOTYPE_5_19

#endif
