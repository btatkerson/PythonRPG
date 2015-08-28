#!/usr/bin/python3

import copy
from core.verbose import verbose

class catalog(verbose):
    def __init__(self):
        verbose.__init__(self, 1)
        self.__custom_number_index = 1
        self.__catalog = {}

    def get_catalog(self):
        return dict(self.__catalog)

    def find_resource(self, res_ref=None):
        temp_ref = clean_res_ref(res_ref)
        try:
            return self.__catalog[temp_ref]
        except KeyError:
            self.verbo(("Resource \'", clean_res_ref(temp_ref), "\' not found."))
            return None

    def copy_resource(self, res_ref=None):
        if self.find_resource(res_ref):
            return copy.copy(self.find_resource(res_ref))
        return None

    def is_resource(self, res_ref=None):
        if self.find_resource(res_ref):
            return True
        return False

    def add_resource(self,res_ref=None,resource=None, override=False):
        if self.is_resource(res_ref):
            if not override:

                self.verbo(("Resource \'",clean_res_ref(res_ref),"\' already exists"))
                return 0
            elif resource is not None:
                self.__catalog[clean_res_ref(res_ref)]=resource
                return 1

            return 0

        else:
            if resource is not None:
                self.__catalog[clean_res_ref(res_ref)]=resource
                self.verbo(("Resource \'",clean_res_ref(res_ref),"\' added to catalog."))
                return 1
            return 0

    def pop_resource(self, res_ref=None):
        if self.is_resource(res_ref):
            return self.__catalog.pop(clean_res_ref(res_ref))

    def remove_resource(self, res_ref=None):
        if self.is_resource(res_ref):
            self.__catalog.pop(clean_res_ref(res_ref))
            return 1

        self.verbo(("Resource \'", clean_res_ref(res_ref), "\' not found."))
        return 0


def clean_res_ref(res_ref=None):
    res_ref = res_ref.lower()
    acceptable_characters = [chr(i) for i in list(range(48,58))+list(range(97,123))]+['_']
    temp = ''
    for i in res_ref:
        if i == " ":
            i = "_"
        if i in acceptable_characters:
            temp+=i

    return temp


class blueprint():
    def __init__(self, prefix=None, custom=None):
        self.prefix = None
        self.__set_prefix(prefix)

        self.custom = None
        self.__set_custom(custom)

        self.ref_name = None

        self.__suffix = ''
        self.__suffix_gen = self.__num_suffix_str_generator()

        self.set_ref_name()

    def __num_suffix_str_generator(self):
        temp_num = 1
        while True:
            temp = list(str(temp_num))
            while len(temp) < 4:
                temp.insert(0,'0')
            temp_num += 1
            yield '_'+''.join(temp)

    def __reset_num_suffix_str_generator(self):
        self.__suffix_gen = self.__num_suffix_str_generator()

    def __get_num_suffix_str(self):
        self.__suffix = next(self.__suffix_gen)

    def __set_prefix(self,prefix=None):
        pref = clean_res_ref(prefix)
        if pref[-1] != '_':
            pref += '_'

        if len(pref) > 0 and pref != '_':
            self.prefix = pref
        else:
            self.prefix = 'bp_gen_'

    def get_prefix(self):
        return self.prefix

    def __set_custom(self,custom=None):
        if custom:
            self.custom = True
        else:
            self.custom = False

    def is_custom(self):
        return self.custom

    def set_ref_name(self, ref_name=None, ignore_catalog=False):
        temp_old_name = ''
        reset_catalog_res_ref = False
        if self.ref_name and not ignore_catalog:
            temp_old_name = self.get_res_ref()
            if cat.find_resource(temp_old_name) == self:
                reset_catalog_res_ref = True
                self.__suffix = ''
                self.__reset_num_suffix_str_generator()
                
        if type(ref_name) == str:
            self.ref_name = clean_res_ref(ref_name)
            while cat.is_resource(self.get_res_ref()) and not ignore_catalog:
                self.__get_num_suffix_str()
            self.__reset_num_suffix_str_generator()
        else:
            self.ref_name = 'generic'
            while cat.is_resource(self.get_res_ref()):
                self.__get_num_suffix_str()
            self.__reset_num_suffix_str_generator()

        if temp_old_name != self.get_res_ref() and reset_catalog_res_ref:
            cat.remove_resource(temp_old_name)
            self.add_self_to_catalog()


    def get_ref_name(self):
        return self.ref_name

    def get_res_ref(self):
        if self.custom:
            cust = 'cust_'
        else:
            cust = ""

        return self.prefix + cust + self.ref_name + self.__suffix

    def add_self_to_catalog(self, override=False):
        self.set_ref_name(self.ref_name, override)
        if cat.is_resource(self.get_res_ref()):
            if override:
                cat.verbo_Activate()
                cat.add_resource(self.get_res_ref(), self, True)
                return 1
            else:
                '''
                This will only add itself to the catalog if the address of the object is unique in the catalog.

                Both the keys and items of the universal catalog will be unique in order to keep statistics 
                separated.

                This will prevent heartache
                '''
                if self not in cat.get_catalog().items():
                    self.set_ref_name(self.ref_name, False)
                    cat.verbo_Activate()
                    cat.add_resource(self.get_res_ref(), self)
                    return 1
                cat.verbo_Activate()
                return 0
        else:
            cat.verbo_Activate()
            cat.add_resource(self.get_res_ref(), self)
            return 1
        cat.verbo_Activate()

    def copy_self_to_catalog(self, override=False):
        cat.verbo_Deactivate()
        if cat.is_resource(self.get_res_ref()):
            if override:
                cat.verbo_Activate()
                cat.add_resource(self.get_res_ref(), copy.copy(self), True)
                return 1
            else:
                self.set_ref_name(self.ref_name, override)
                cat.verbo_Activate()
                cat.add_resource(self.get_res_ref(), copy.copy(self))
                return 0
        else:
            cat.verbo_Activate()
            cat.add_resource(self.get_res_ref(), copy.copy(self))
        cat.verbo_Activate()


cat = catalog()
