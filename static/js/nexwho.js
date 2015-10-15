var _countries = ["United States", "Canada", "United Kingdom", "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Ascension Island", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Camaroon", "Cambodia", "Cameroon", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Cote D Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Federated States of Micronesia", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "Gabon", "Gaza Strip", "Georgia", "Germany", "Ghana", "Gibralter", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jarvis Island", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea (Peoples Republic of)", "Korea (Republic of)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Cypress", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Vincent and the Grenadines", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Serbia and Montenegro", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia", "South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Kitts and Nevis", "St. Lucia", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "The Gambia", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tristan da Cunha", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Viet Nam", "Virgin Islands (U.K.)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "West Bank", "Western Sahara", "Western Samoa", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"];
var _sexualities = ["Straight", "Gay", "Lesbian", "Bisexual"];
var _ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89];
var _genders = ["Female", "Male", "Trans"];
var _words = ["fuck", "nude", "porn", "bitch", "slut", "pussy", "pussie", "vagina", "naked"];
var _ws, _pc, _localStream, _remoteStream, _dataChannel, _myInfo, _inChat = false;
var RTCPeerConnection, getUserMedia, attachMediaStream;



function Onload() {
    CreateSelect("uAge", _ages);
    CreateSelect("uGender", _genders);
    CreateSelect("uSex", _sexualities);
    CreateSelect("uCountry", _countries);
}

function OnReg() {
    if (navigator.mozGetUserMedia) {
        RTCSessionDescription = mozRTCSessionDescription;
        RTCIceCandidate = mozRTCIceCandidate;
        getUserMedia = navigator.mozGetUserMedia.bind(navigator);
        attachMediaStream = function (element, stream) {
            element.mozSrcObject = stream;
            element.play();
        };

        reattachMediaStream = function (to, from) {
            to.mozSrcObject = from.mozSrcObject;
            to.play();
        };
        MediaStream.prototype.getVideoTracks = function () {
            return [];
        };

        MediaStream.prototype.getAudioTracks = function () {
            return [];
        };
    } else if (navigator.webkitGetUserMedia) {
        RTCPeerConnection = webkitRTCPeerConnection;
        getUserMedia = navigator.webkitGetUserMedia.bind(navigator);
        attachMediaStream = function (_element, _stream) {
            _element.src = webkitURL.createObjectURL(_stream);
            _element.play();
        };
        if (!webkitMediaStream.prototype.getVideoTracks) {
            webkitMediaStream.prototype.getVideoTracks = function () {
                return this.videoTracks;
            };
        }
        if (!webkitMediaStream.prototype.getAudioTracks) {
            webkitMediaStream.prototype.getAudioTracks = function () {
                return this.audioTracks;
            };
        }
    }
    else if (!navigator.getUserMedia) {
        ShowAlert("regAlert", "Your browser is not HTML5 compatible.");
        return;
    }
    var _age = document.getElementById("uAge").value;
    var _gender = document.getElementById("uGender").value;
    var _sex = document.getElementById("uSex").value;
    var _country = document.getElementById("uCountry").value;
    if (_age.length > 0 && _gender.length > 0 && _sex.length > 0 && _country.length > 0) {
        _myInfo = "{\"type\":\"user\",\"data\":\"" + _age + "*" + _gender + "*" + _sex + "*" + _country + "\"}";
        document.getElementById("regBtn").value = "Connecting...";
        document.getElementById("regBtn").disabled = true;
        _ws = new WebSocket("ws://www.nexwho.com:2099/echo");
        _ws.onmessage = function (e) {
            var _json = JSON.parse(e.data);
            switch (_json.type) {
                case "command":
                    switch (_json.data) {
                        case "0":
                            ShowAlert("regAlert", "Your IP is blocked. Please wait for 24 hrs.");
                            break;
                        case
                            "1":
                            ShowAlert("regAlert", "You are using NexWho already.");
                            chat.CreatePeerConnection(_json.data);
                            break;
                        case "4.1":
                            ShowNewMsg("One match is found. Connecting to the match...", "System");
                            CreatePeerConnection(_json.data);
                            break;
                        case "4.2":
                            ShowNewMsg("One match is found. Connecting to the match...", "System");
                            CreatePeerConnection(_json.data);
                            break;
                        case "6":
                            ShowNewMsg("No idle chatter at this moment. We will match you as soon as there is one.", "System");
                            break;
                        case "1.2":
                            chat.ShowMsg("Repondent start to wait for the new match ...");
                            chat.CreatePeerConnection(_json.data);
                            break;
                        case "2":
                            break;
                    }
                    break;
                case "offer":
                    _pc.setRemoteDescription(new RTCSessionDescription(_json));
                    _pc.createAnswer(SetLocalAndSendMessage);
                    break;
                case "answer":
                    _pc.setRemoteDescription(new RTCSessionDescription(_json));
                    break;
                case "candidate":
                    var candidate = new RTCIceCandidate({ sdpMLineIndex: _json.label, candidate: _json.candidate });
                    if (_pc) {
                        _pc.addIceCandidate(candidate);
                    }
                    if (_inChat == false) {
                        _inChat = true;
                    }
                    break;
            };
        };

        _ws.onopen = function () {
            getUserMedia({ audio: true, video: true }, OnMediaSuccess, OnMediaError);
        };

        _ws.onclose = function () {
            ShowAlert("alert", "The connection to the server is closed.");
        };
    }
    else {
        ShowAlert("regAlert", "Please finish all items");
    };
}

function OnMediaSuccess(e) {
    _localStream = e;
    attachMediaStream(document.getElementById("myVid"), e);
    document.getElementById("homeZone").style.display = "none";
    document.getElementById("chatZone").style.display = "block";
    _ws.send(_myInfo);
    ShowNewMsg("Waiting for new match...", "System");
}

function OnMediaError () {
    ShowAlert("regAlert", "failed to find your webcam.");
}

function CreateSelect(_id, _array) {
    var _value = 0;
    var _select = document.getElementById(_id);
    var _str = "";
    for (var _index = 0; _index < _array.length; _index++) {
        _str += "<option value='" + _value + "'>" + _array[_index] + "</option>";
        _value += 1;
    };
    _select.innerHTML = _str;
}

function ShowAlert(_id, _msg) {
    document.getElementById(_id).innerHTML = _msg;
    document.getElementById(_id).style.display = "block";
    setTimeout(function () {HideAlert(_id) }, 8000);
}

function HideAlert(_id) {
    document.getElementById(_id).innerHTML = "";
    document.getElementById(_id).style.display = "none";
}

function ShowNewMsg(_msg, _name) {
    var _date = new Date();
    document.getElementById("msgs").innerHTML += _date.getHours() + ":" + _date.getMinutes() + ":" + _date.getSeconds() + "<br/><b>" + _name + "</b>: " + _msg + "<br/><br/>";
    document.getElementById("msgs").scrollTop = document.getElementById("msgs").scrollHeight;
}

function CreatePeerConnection(_code) {
    DisposeEnvironment();
    var _config = { "iceServers": [{ "url": "stun:stun.l.google.com:19302" }] };
    _options = { optional: [{ RtpDataChannels: true }] };
    _pc = new  RTCPeerConnection(_config, _options);
    _pc.onicecandidate = OnICE;
    _pc.addStream(_localStream);
    _pc.onaddstream = OnRemoteStream;
    setInterval(function () {
        if (_pc && _pc.iceConnectionState && _pc.iceConnectionState === "disconnected") {
            if (_inChat == true) {
                ShowNewMsg("The chatter has left.", "System");
                _inChat = false;
            }
        }
    }, 1000);
    if (_code == "4.1") {
        _dataChannel = _pc.createDataChannel("nexWho", { reliable: false });
        _dataChannel.onmessage = OnClientMsgReceived;
        _dataChannel.onopen = OnOpenDataChannel;
        _dataChannel.onclose = OnCloseDataChannel;
        _dataChannel.onerror = OnErrorDataChannel;
        _pc.createOffer(SetLocalAndSendMessage);
        return true;
    }
    _pc.ondatachannel = OnInDataChannel;
}

function DisposeEnvironment() {
    if (_pc) {
        _pc.close();
        _pc = null;
    }
    if (_dataChannel) {
        _dataChannel.close();
        _dataChannel = null;
    }
}

function OnICE(e){
    if (e.candidate) {
        var _ice = { type: 'candidate', label: event.candidate.sdpMLineIndex, id: event.candidate.sdpMid, candidate: event.candidate.candidate };
        var _str = JSON.stringify(_ice);   
        _ws.send(_str);
    } 
}

function OnRemoteStream(e) {
    attachMediaStream(document.getElementById("youVid"), e.stream);
    document.getElementById("youVid").style.display = "block";
    document.getElementById("youInfo").innerHTML = "<input id='nextBtn' class='regBtn' type='button' value='Next' onclick='OnNext()'/><input id='reportBtn' class='regBtn' type='button' value='Report' onclick='OnReport(this)'/>";
}

function OnClientMsgReceived(e) {
    ShowNewMsg(e.data, "You");
}

function SetLocalAndSendMessage(_desc) {
    _pc.setLocalDescription(_desc);
    _ws.send(JSON.stringify(_desc));
}

function OnInDataChannel(e) {    
    _dataChannel = e.channel;
    _dataChannel.onmessage = OnClientMsgReceived;
    _dataChannel.onopen = OnOpenDataChannel;
    _dataChannel.onclose = OnCloseDataChannel;
    _dataChannel.onerror = OnErrorDataChannel;
}

function OnCloseDataChannel() {
    ShowNewMsg("The chatter has left", "System");
}

function OnOpenDataChannel() {
    ShowNewMsg("You could type text messages to the chatter now.", "System");    
    document.getElementById("msgInput").addEventListener("keyup", function (e) {
        if (e.keyCode == 13) {
            OnSend();
        }
    }, false);
}
function OnErrorDataChannel() {
    ShowNewMsg("The datachannel get errored.", "System");
}

function OnNext() {
    document.getElementById("youInfo").innerHTML = "";
    document.getElementById("msgs").innerHTML = "";
    document.getElementById("youVid").style.display = "none";
    DisposeEnvironment();
    _ws.send("{\"data\":\"3\",\"type\":\"command\"}");
    ShowNewMsg("Waiting for new match...", "System");
}

function OnReport(e) {
    document.getElementById("reportBtn").disabled = true;
    _ws.send("{\"data\":\"8\",\"type\":\"command\"}");
}
    
function OnSend() {
    if (_dataChannel && document.getElementById("msgInput").value.length > 0) {
        _dataChannel.send(document.getElementById("msgInput").value);        
        ShowNewMsg(document.getElementById("msgInput").value, "Me");
        document.getElementById("msgInput").value = "";
    }
}

    