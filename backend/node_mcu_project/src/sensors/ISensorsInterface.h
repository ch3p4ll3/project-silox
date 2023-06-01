#pragma once

#include "Arduino.h"


class ISensorsInterface {
    protected:
        String slug;
        String name;
        int silosId;
        double value;

    public:
        void setSlug(String slug);
        void setName(String name);
        void setValue(double value);

        String getSlug();
        String getName();
        double getValue();

        virtual String toJson();
        String getTopic();
};