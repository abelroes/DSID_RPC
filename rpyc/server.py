import rpyc
import json
port = 18861

class Classe(object):
    def __init__(self):
        self.a = "20"
        self.b = 2
        self.c = "teste"

    def toJSON(self):
        return '{"a":"20", "b":2, "c":"teste" }'

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    # operação sem argumentos e sem valor de retorno
    def exposed_method1(self): 
        pass

    # operação com um argumento long e valor de retorno long 
    def exposed_method2(self, number): 
        return number*number

    # operação com oito argumentos long e valor de retorno long 
    def exposed_method3(self, n1, n2, n3, n4, n5, n6, n7, n8): 
        return int((n1+n2+n3+n4+n5+n6+n7+n8)/8 )
    
    # operação com um argumento String e valor de retorno String (4 args)
    def exposed_method4(self, s1, s2, s3, s4):
        return "never gonna give you up" #s1+s2+s3+s4

    # operação com um argumento String e valor de retorno String (8 args)
    def exposed_method5(self, s1,s2,s3,s4,s5,s6,s7,s8):
        return "never gonna let you down" #s1+s2+s3+s4+s5+s6+s7+s8

    # operação com um argumento String e valor de retorno String (16 args)
    def exposed_method6(self,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16):
        return "never gonna run around " #s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16

    # operação com um argumento String e valor de retorno String (32 args)
    def exposed_method7(self,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32):
        return "and desert you" #s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20+s21+s22+s23+s24+s25+s26+s27+s28+s29+s30+s31+s32

    # operação com um argumento String e valor de retorno String (64 args)
    def exposed_method8(self,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64):
        return "Never gonna make you cry"#s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20+s21+s22+s23+s24+s25+s26+s27+s28+s29+s30+s31+s32+s33+s34+s35+s36+s37+s38+s39+s40+s41+s42+s43+s44+s45+s46+s47+s48+s49+s50+s51+s52+s53+s54+s55+s56+s57+s58+s59+s60+s61+s62+s63+s64

    # operação com um argumento String e valor de retorno String (128 args)
    def exposed_method9(self,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89,s90,s91,s92,s93,s94,s95,s96,s97,s98,s99,s100,s101,s102,s103,s104,s105,s106,s107,s108,s109,s110,s111,s112,s113,s114,s115,s116,s117,s118,s119,s120,s121,s122,s123,s124,s125,s126,s127,s128):
        return "Never gonna say goodbye"#s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20+s21+s22+s23+s24+s25+s26+s27+s28+s29+s30+s31+s32+s33+s34+s35+s36+s37+s38+s39+s40+s41+s42+s43+s44+s45+s46+s47+s48+s49+s50+s51+s52+s53+s54+s55+s56+s57+s58+s59+s60+s61+s62+s63+s64+s65+s66+s67+s68+s69+s70+s71+s72+s73+s74+s75+s76+s77+s78+s79+s80+s81+s82+s83+s84+s85+s86+s87+s88+s89+s90+s91+s92+s93+s94+s95+s96+s97+s98+s99+s100+s101+s102+s103+s104+s105+s106+s107+s108+s109+s110+s111+s112+s113+s114+s115+s116+s117+s118+s119+s120+s121+s122+s123+s124+s125+s126+s127+s128

    # operação com um argumento String e valor de retorno String (254 args)
    def exposed_method10(self, s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89,s90,s91,s92,s93,s94,s95,s96,s97,s98,s99,s100,s101,s102,s103,s104,s105,s106,s107,s108,s109,s110,s111,s112,s113,s114,s115,s116,s117,s118,s119,s120,s121,s122,s123,s124,s125,s126,s127,s128,s129,s130,s131,s132,s133,s134,s135,s136,s137,s138,s139,s140,s141,s142,s143,s144,s145,s146,s147,s148,s149,s150,s151,s152,s153,s154,s155,s156,s157,s158,s159,s160,s161,s162,s163,s164,s165,s166,s167,s168,s169,s170,s171,s172,s173,s174,s175,s176,s177,s178,s179,s180,s181,s182,s183,s184,s185,s186,s187,s188,s189,s190,s191,s192,s193,s194,s195,s196,s197,s198,s199,s200,s201,s202,s203,s204,s205,s206,s207,s208,s209,s210,s211,s212,s213,s214,s215,s216,s217,s218,s219,s220,s221,s222,s223,s224,s225,s226,s227,s228,s229,s230,s231,s232,s233,s234,s235,s236,s237,s238,s239,s240,s241,s242,s243,s244,s245,s246,s247,s248,s249,s250,s251,s252,s253,s254):
        return "Never gonna tell a lie and hurt you" # s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20+s21+s22+s23+s24+s25+s26+s27+s28+s29+s30+s31+s32+s33+s34+s35+s36+s37+s38+s39+s40+s41+s42+s43+s44+s45+s46+s47+s48+s49+s50+s51+s52+s53+s54+s55+s56+s57+s58+s59+s60+s61+s62+s63+s64+s65+s66+s67+s68+s69+s70+s71+s72+s73+s74+s75+s76+s77+s78+s79+s80+s81+s82+s83+s84+s85+s86+s87+s88+s89+s90+s91+s92+s93+s94+s95+s96+s97+s98+s99+s100+s101+s102+s103+s104+s105+s106+s107+s108+s109+s110+s111+s112+s113+s114+s115+s116+s117+s118+s119+s120+s121+s122+s123+s124+s125+s126+s127+s128+s129+s130+s131+s132+s133+s134+s135+s136+s137+s138+s139+s140+s141+s142+s143+s144+s145+s146+s147+s148+s149+s150+s151+s152+s153+s154+s155+s156+s157+s158+s159+s160+s161+s162+s163+s164+s165+s166+s167+s168+s169+s170+s171+s172+s173+s174+s175+s176+s177+s178+s179+s180+s181+s182+s183+s184+s185+s186+s187+s188+s189+s190+s191+s192+s193+s194+s195+s196+s197+s198+s199+s200+s201+s202+s203+s204+s205+s206+s207+s208+s209+s210+s211+s212+s213+s214+s215+s216+s217+s218+s219+s220+s221+s222+s223+s224+s225+s226+s227+s228+s229+s230+s231+s232+s233+s234+s235+s236+s237+s238+s239+s240+s241+s242+s243+s244+s245+s246+s247+s248+s249+s250+s251+s252+s253+s254

    def exposed_method11(self):
        return Classe().toJSON()

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=port)
    t.start()