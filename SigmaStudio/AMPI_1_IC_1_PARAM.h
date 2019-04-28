/*
 * File:           C:\Users\Stefan\Documents\RPI\AMPI\Python_AMPI\SigmaStudio\AMPI_1_IC_1_PARAM.h
 *
 * Created:        Monday, February 18, 2019 5:39:36 PM
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


/* Module Square1 - Square wave*/
#define COUNT_SQUARE1                                  3
#define DEVICE_SQUARE1                                 "IC1"
#define STATIC_ADDR_SQUARE1_MASK                       0
#define STATIC_FIXPT_SQUARE1_MASK                      0x000000FF
#define STATIC_VALUE_SQUARE1_MASK                      SIGMASTUDIOTYPE_INTEGER_CONVERT(255)
#define STATIC_TYPE_SQUARE1_MASK                       SIGMASTUDIOTYPE_INTEGER
#define ADDR_SQUARE1_FREQ                              1
#define FIXPT_SQUARE1_FREQ                             0x000258BF
#define VALUE_SQUARE1_FREQ                             SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0183333333333333)
#define TYPE_SQUARE1_FREQ                              SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SQUARE1_ON                                2
#define FIXPT_SQUARE1_ON                               0x00000000
#define VALUE_SQUARE1_ON                               SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_SQUARE1_ON                                SIGMASTUDIOTYPE_FIXPOINT

/* Module Triangle1 - Triangle wave*/
#define COUNT_TRIANGLE1                                7
#define DEVICE_TRIANGLE1                               "IC1"
#define ADDR_TRIANGLE1_TRI0                            3
#define FIXPT_TRIANGLE1_TRI0                           0x00000000
#define VALUE_TRIANGLE1_TRI0                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_TRIANGLE1_TRI0                            SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_TRI1                            4
#define FIXPT_TRIANGLE1_TRI1                           0x00800000
#define VALUE_TRIANGLE1_TRI1                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_TRIANGLE1_TRI1                            SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_TRI2                            5
#define FIXPT_TRIANGLE1_TRI2                           0x00000000
#define VALUE_TRIANGLE1_TRI2                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_TRIANGLE1_TRI2                            SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_TRI3                            6
#define FIXPT_TRIANGLE1_TRI3                           0xFF800000
#define VALUE_TRIANGLE1_TRI3                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-1)
#define TYPE_TRIANGLE1_TRI3                            SIGMASTUDIOTYPE_FIXPOINT
#define STATIC_ADDR_TRIANGLE1_MASK                     7
#define STATIC_FIXPT_TRIANGLE1_MASK                    0x00000003
#define STATIC_VALUE_TRIANGLE1_MASK                    SIGMASTUDIOTYPE_INTEGER_CONVERT(3)
#define STATIC_TYPE_TRIANGLE1_MASK                     SIGMASTUDIOTYPE_INTEGER
#define ADDR_TRIANGLE1_FREQ                            8
#define FIXPT_TRIANGLE1_FREQ                           0x0004B17E
#define VALUE_TRIANGLE1_FREQ                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0366666666666667)
#define TYPE_TRIANGLE1_FREQ                            SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_ON                              9
#define FIXPT_TRIANGLE1_ON                             0x00000000
#define VALUE_TRIANGLE1_ON                             SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_TRIANGLE1_ON                              SIGMASTUDIOTYPE_FIXPOINT

/* Module Square1_2 - Square wave*/
#define COUNT_SQUARE1_2                                3
#define DEVICE_SQUARE1_2                               "IC1"
#define STATIC_ADDR_SQUARE1_2_MASK                     10
#define STATIC_FIXPT_SQUARE1_2_MASK                    0x000000FF
#define STATIC_VALUE_SQUARE1_2_MASK                    SIGMASTUDIOTYPE_INTEGER_CONVERT(255)
#define STATIC_TYPE_SQUARE1_2_MASK                     SIGMASTUDIOTYPE_INTEGER
#define ADDR_SQUARE1_2_FREQ                            11
#define FIXPT_SQUARE1_2_FREQ                           0x00025761
#define VALUE_SQUARE1_2_FREQ                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0182916666666667)
#define TYPE_SQUARE1_2_FREQ                            SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SQUARE1_2_ON                              12
#define FIXPT_SQUARE1_2_ON                             0x00000000
#define VALUE_SQUARE1_2_ON                             SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_SQUARE1_2_ON                              SIGMASTUDIOTYPE_FIXPOINT

/* Module Triangle1_2 - Triangle wave*/
#define COUNT_TRIANGLE1_2                              7
#define DEVICE_TRIANGLE1_2                             "IC1"
#define ADDR_TRIANGLE1_2_TRI0                          13
#define FIXPT_TRIANGLE1_2_TRI0                         0x00000000
#define VALUE_TRIANGLE1_2_TRI0                         SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_TRIANGLE1_2_TRI0                          SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_2_TRI1                          14
#define FIXPT_TRIANGLE1_2_TRI1                         0x00800000
#define VALUE_TRIANGLE1_2_TRI1                         SIGMASTUDIOTYPE_FIXPOINT_CONVERT(1)
#define TYPE_TRIANGLE1_2_TRI1                          SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_2_TRI2                          15
#define FIXPT_TRIANGLE1_2_TRI2                         0x00000000
#define VALUE_TRIANGLE1_2_TRI2                         SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_TRIANGLE1_2_TRI2                          SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_2_TRI3                          16
#define FIXPT_TRIANGLE1_2_TRI3                         0xFF800000
#define VALUE_TRIANGLE1_2_TRI3                         SIGMASTUDIOTYPE_FIXPOINT_CONVERT(-1)
#define TYPE_TRIANGLE1_2_TRI3                          SIGMASTUDIOTYPE_FIXPOINT
#define STATIC_ADDR_TRIANGLE1_2_MASK                   17
#define STATIC_FIXPT_TRIANGLE1_2_MASK                  0x00000003
#define STATIC_VALUE_TRIANGLE1_2_MASK                  SIGMASTUDIOTYPE_INTEGER_CONVERT(3)
#define STATIC_TYPE_TRIANGLE1_2_MASK                   SIGMASTUDIOTYPE_INTEGER
#define ADDR_TRIANGLE1_2_FREQ                          18
#define FIXPT_TRIANGLE1_2_FREQ                         0x0004B2DB
#define VALUE_TRIANGLE1_2_FREQ                         SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.0367083333333333)
#define TYPE_TRIANGLE1_2_FREQ                          SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_TRIANGLE1_2_ON                            19
#define FIXPT_TRIANGLE1_2_ON                           0x00000000
#define VALUE_TRIANGLE1_2_ON                           SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0)
#define TYPE_TRIANGLE1_2_ON                            SIGMASTUDIOTYPE_FIXPOINT

/* Module Single 1 - Single Volume*/
#define COUNT_SINGLE1                                  2
#define DEVICE_SINGLE1                                 "IC1"
#define ADDR_SINGLE1_1                                 20
#define FIXPT_SINGLE1_1                                0x00101D3F
#define VALUE_SINGLE1_1                                SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.125892541179417)
#define TYPE_SINGLE1_1                                 SIGMASTUDIOTYPE_FIXPOINT
#define ADDR_SINGLE1                                   21
#define FIXPT_SINGLE1                                  0x00101D3F
#define VALUE_SINGLE1                                  SIGMASTUDIOTYPE_FIXPOINT_CONVERT(0.125892541179417)
#define TYPE_SINGLE1                                   SIGMASTUDIOTYPE_FIXPOINT

#endif